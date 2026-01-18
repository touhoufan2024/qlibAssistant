import fire
import akshare as ak
import pandas as pd
import os
import datetime
import concurrent.futures
from tqdm import tqdm

class CSI300FullManager:
    """
    沪深300 全数据版 (包含市盈率、总市值等财务指标)
    
    使用方法:
    python csi300_full.py download --days=30
    """

    def __init__(self, save_dir="./csi300_full_data"):
        self.save_dir = save_dir
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def _get_styled_code(self, code):
        """SH600519"""
        code = str(code)
        if code.startswith("6"): return f"SH{code}"
        if code.startswith(("0", "3")): return f"SZ{code}"
        return f"UNKNOWN{code}"

    def _download_worker(self, code, name, start_str, end_str):
        try:
            # ==========================================
            # 1. 获取基础行情 (开/高/低/收/量)
            # ==========================================
            df_price = ak.stock_zh_a_hist(
                symbol=code, period="daily", start_date=start_str, end_date=end_str, adjust="qfq"
            )
            if df_price.empty: return None

            # 基础清洗
            df_price.rename(columns={'日期': 'date', '收盘': '最新价', '开盘': '今开', 
                                     '最高': '最高', '最低': '最低', '成交量': '成交量', 
                                     '成交额': '成交额', '涨跌幅': '涨跌幅', '换手率': '换手率'}, inplace=True)
            
            # 计算衍生字段
            df_price['昨收'] = df_price['最新价'].shift(1).fillna(df_price['今开'])
            df_price['涨跌额'] = df_price['最新价'] - df_price['昨收']
            df_price['振幅'] = ((df_price['最高'] - df_price['最低']) / df_price['昨收'] * 100).round(2)
            
            # 转换日期格式以便合并 (YYYY-MM-DD)
            df_price['date'] = pd.to_datetime(df_price['date'])

            # ==========================================
            # 2. 获取估值指标 (市盈率/市净率/总市值)
            # ==========================================
            # 注意：这个接口不需要 start/end，它返回所有历史，我们需要自己过滤
            # 乐咕网接口: stock_a_indicator_lg
            try:
                df_val = ak.stock_a_indicator_lg(symbol=code)
                if not df_val.empty:
                    # 过滤日期
                    df_val['trade_date'] = pd.to_datetime(df_val['trade_date'])
                    
                    # 筛选时间范围 (稍微放宽一点防止对不上)
                    mask = (df_val['trade_date'] >= pd.to_datetime(start_str)) & \
                           (df_val['trade_date'] <= pd.to_datetime(end_str))
                    df_val = df_val.loc[mask].copy()

                    # 重命名以符合你的截图习惯
                    # pe_ttm: 滚动市盈率, total_mv: 总市值(万)
                    df_val.rename(columns={
                        'trade_date': 'date', 
                        'pe_ttm': '市盈率', 
                        'total_mv': '总市值' # 注意：源数据单位通常是万
                    }, inplace=True)
                    
                    # 只保留需要的列
                    df_val = df_val[['date', '市盈率', '总市值']]
            except:
                # 如果获取失败，创建一个空的 DataFrame，防止程序崩溃
                df_val = pd.DataFrame(columns=['date', '市盈率', '总市值'])

            # ==========================================
            # 3. 合并两张表 (Merge)
            # ==========================================
            # 类似于 Excel 的 VLOOKUP，根据 'date' 匹配
            df_final = pd.merge(df_price, df_val, on='date', how='left')

            # 格式化日期回字符串
            df_final['日期'] = df_final['date'].dt.strftime('%Y-%m-%d')
            
            # 补充静态列
            df_final['代码'] = self._get_styled_code(code)
            df_final['名称'] = name
            
            # 处理市值的单位 (原数据通常是万，转为亿可能更好看，这里保持原样或根据需求改)
            # 假设我们想要截图里的数值效果，通常保留原值即可
            
            # ==========================================
            # 4. 整理列顺序
            # ==========================================
            target_cols = [
                '日期', '代码', '名称', 
                '最新价', '涨跌幅', '涨跌额', 
                '成交量', '成交额', 
                '振幅', '最高', '最低', '今开', '昨收', 
                '换手率', '市盈率', '总市值' 
            ]
            final_cols = [c for c in target_cols if c in df_final.columns]
            
            # 保存
            file_path = os.path.join(self.save_dir, f"{self._get_styled_code(code)}.csv")
            df_final[final_cols].round(2).to_csv(file_path, index=False)
            
            return code
            
        except Exception as e:
            # print(f"Error {code}: {e}") # 调试用
            return None

    def download(self, days=30, workers=4):
        """
        [下载] 包含市盈率和总市值的全数据
        注意：因为多请求了一个接口，速度会比之前慢一倍，建议 workers 设小一点防止封IP
        """
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=days + 15)
        start_str = start_date.strftime("%Y%m%d")
        end_str = end_date.strftime("%Y%m%d")
        
        print(f"🚀 准备下载全维度数据: {start_str} -> {end_str}")
        print("正在获取成分股...")
        
        try:
            cons = ak.index_stock_cons(symbol="000300")
            # 简单匹配名称逻辑
            code_col = next((c for c in ['品种代码', 'variety', '代码'] if c in cons.columns), None)
            name_col = next((c for c in ['品种名称', 'name', '名称'] if c in cons.columns), None)
            
            # 如果没有名称列，还是得去全市场匹配一下（此处简化，假设有）
            if not name_col:
                # 兜底逻辑：不显示名称或只显示代码
                stock_info = [(c, "未知") for c in cons[code_col].tolist()]
            else:
                stock_info = list(zip(cons[code_col], cons[name_col]))
                
        except Exception:
            print("获取名单失败")
            return

        print(f"开始下载 {len(stock_info)} 只股票 (速度较慢，请耐心等待)...")
        
        success = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            future_to_item = {
                executor.submit(self._download_worker, item[0], item[1], start_str, end_str): item 
                for item in stock_info
            }
            
            for future in tqdm(concurrent.futures.as_completed(future_to_item), total=len(stock_info)):
                if future.result():
                    success += 1

        print(f"\n✅ 完成！已保存至 {self.save_dir}")

if __name__ == "__main__":
    fire.Fire(CSI300FullManager)