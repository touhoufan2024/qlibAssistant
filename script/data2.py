import fire
import akshare as ak
import pandas as pd
import os
import datetime
import concurrent.futures
from tqdm import tqdm

class CSI300ProManager:
    """
    沪深300 专业版数据管理工具 (仿东方财富截图格式)
    
    使用方法:
    1. 下载过去30天数据:
       python csi300_pro.py download --days=30
       
    2. 查询本地数据:
       python csi300_pro.py query 600519
    """

    def __init__(self, save_dir="./csi300_pro_data"):
        self.save_dir = save_dir
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def _get_styled_code(self, code):
        """生成截图风格的大写前缀代码 (SH600519)"""
        code = str(code)
        if code.startswith("6"): return f"SH{code}"
        if code.startswith(("0", "3")): return f"SZ{code}"
        return f"UNKNOWN{code}"

    def _download_worker(self, code, name, start_str, end_str):
        """下载并清洗为截图格式"""
        try:
            # 1. 下载历史数据
            df = ak.stock_zh_a_hist(
                symbol=code, 
                period="daily", 
                start_date=start_str, 
                end_date=end_str, 
                adjust="qfq"
            )
            
            if df.empty: return None

            # 2. 计算缺失的关键字段 (模仿行情软件逻辑)
            # 计算昨收：把收盘价向下移动一行
            df['昨收'] = df['收盘'].shift(1)
            # 第一天的昨收没法算，只能用开盘价暂代或填空
            df['昨收'] = df['昨收'].fillna(df['开盘'])

            # 计算涨跌额
            df['涨跌额'] = df['收盘'] - df['昨收']

            # 计算振幅: (最高-最低) / 昨收 * 100
            df['振幅'] = ((df['最高'] - df['最低']) / df['昨收'] * 100).round(2)

            # 3. 构造符合截图的列
            # 添加静态列
            df['代码'] = self._get_styled_code(code)
            df['名称'] = name

            # 4. 重命名列 (完全对齐截图表头)
            rename_map = {
                '日期': '日期',
                '收盘': '最新价',
                '开盘': '今开',
                '最高': '最高',
                '最低': '最低',
                '成交量': '成交量',
                '成交额': '成交额',
                '涨跌幅': '涨跌幅',
                '换手率': '换手率'
            }
            df.rename(columns=rename_map, inplace=True)

            # 5. 按截图习惯排序字段
            # 注意：历史数据无法轻易获取每日的"量比"、"市盈率"、"总市值"，故省略
            target_cols = [
                '日期', '代码', '名称', 
                '最新价', '涨跌幅', '涨跌额', 
                '成交量', '成交额', 
                '振幅', '最高', '最低', '今开', '昨收', 
                '换手率'
            ]
            
            # 确保列都存在
            final_cols = [c for c in target_cols if c in df.columns]
            
            # 6. 保存
            file_path = os.path.join(self.save_dir, f"{self._get_styled_code(code)}.csv")
            # 保留两位小数，看起来更整洁
            df[final_cols].round(2).to_csv(file_path, index=False)
            
            return code
        except Exception:
            return None

    def download(self, days=30, workers=8):
        """
        [下载] 获取过去 N 天的数据，格式仿照东方财富
        """
        # 计算日期
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=days + 10) # 多下几天为了算昨收
        start_str = start_date.strftime("%Y%m%d")
        end_str = end_date.strftime("%Y%m%d")
        
        print(f"🚀 准备下载沪深300历史数据 (仿截图格式): {start_str} -> {end_str}")

        # 获取名单 (含名称)
        print("正在获取成分股名单及名称...")
        try:
            # 使用备用接口获取名称，防止 index_stock_cons 缺名称
            # 先拿代码
            cons = ak.index_stock_cons(symbol="000300")
            
            # 处理列名兼容性
            code_col = next((c for c in ['品种代码', 'variety', '代码'] if c in cons.columns), None)
            name_col = next((c for c in ['品种名称', 'name', '名称'] if c in cons.columns), None)

            if not code_col or not name_col:
                # 如果找不到名称，尝试用实时行情接口拿全量列表匹配 (比较慢但稳)
                print("⚠️ 尝试从全市场列表匹配名称...")
                spot = ak.stock_zh_a_spot_em()
                spot_map = dict(zip(spot['代码'], spot['名称']))
                codes_list = cons[code_col].tolist()
                stock_info = [(c, spot_map.get(str(c), "未知")) for c in codes_list]
            else:
                stock_info = list(zip(cons[code_col], cons[name_col]))
            
            print(f"✅ 获取成功，共 {len(stock_info)} 只股票。")
            
        except Exception as e:
            print(f"❌ 名单获取失败: {e}")
            return

        # 并发下载
        print(f"启动 {workers} 个线程下载...")
        success_count = 0
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            # 提交任务: 传入 code 和 name
            future_to_item = {
                executor.submit(self._download_worker, item[0], item[1], start_str, end_str): item 
                for item in stock_info
            }
            
            for future in tqdm(concurrent.futures.as_completed(future_to_item), total=len(stock_info)):
                if future.result():
                    success_count += 1

        print(f"\n🎉 下载完成！文件已保存在: {self.save_dir}")
        print("💡 提示: 历史数据不包含'市盈率/总市值/量比'等实时变动指标，但交易数据格式已对齐。")

    def query(self, code, date=None):
        """
        [查询] 查询本地数据
        :param code: 股票代码 (如 600519)
        :param date: (可选) 日期
        """
        # 自动处理前缀
        styled_code = self._get_styled_code(str(code).replace("SH","").replace("SZ",""))
        file_path = os.path.join(self.save_dir, f"{styled_code}.csv")
        
        if not os.path.exists(file_path):
            print(f"❌ 未找到文件: {file_path}")
            return

        df = pd.read_csv(file_path)
        
        if date:
            # 精确查询
            row = df[df['日期'] == str(date)]
            if not row.empty:
                print(row.to_string(index=False))
            else:
                print("⚠️ 该日期无数据")
        else:
            # 默认看最近 10 天
            print(f"📊 {styled_code} 最近 10 个交易日数据:")
            # 格式化打印，对齐列宽
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', 1000)
            pd.set_option('display.unicode.east_asian_width', True) # 解决中文对齐
            print(df.tail(10))

if __name__ == "__main__":
    fire.Fire(CSI300ProManager)