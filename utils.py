import tomllib
import os
import shutil
from datetime import datetime
from loguru import logger
import re

def replace_in_file(file_path, regex_pattern, replacement):
    """
    在指定文件中查找匹配正则表达式的部分并替换为指定字符串。

    :param file_path: 要处理的文件路径
    :param regex_pattern: 匹配的正则表达式（支持多行匹配）
    :param replacement: 要替换成的字符串
    """
    try:
        # 读取原始文件内容
        with open(file_path, 'r') as file:
            content = file.read()

        # 使用正则表达式进行替换
        modified_content = re.sub(regex_pattern, replacement, content)

        # 将修改后的内容写入同一个文件
        with open(file_path, 'w') as file:
            file.write(modified_content)

        # print("替换完成！")

    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
    except Exception as e:
        print(f"发生错误：{e}")

def get_config(filename="config.toml"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, filename)
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"配置文件 '{filename}' 未找到，请在路径: {config_path} 下创建该文件。")
    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f) # 标准库解析
    except Exception as e:
        raise Exception(f"TOML 配置文件解析失败: {e}")
    return config

class ConfigLoader:
    def __init__(self, filename="config.toml"):
        self.config = get_config(filename)
        self.output_folder =  os.path.expanduser(os.path.join(self.config["output_path"], datetime.now().strftime("%Y-%m-%d-%H")))
        self.output_folder_is_exist = False

        file_path = os.path.join(self.output_folder, "total_results.md")
        if os.path.exists(file_path):
            os.remove(file_path)

        self.train_s = self.config.get("train", [])[0]
        self.train_e = self.config.get("train", [])[1]
        self.valid_s = self.config.get("valid", [])[0]
        self.valid_e = self.config.get("valid", [])[1]
        self.test_s = self.config.get("test", [])[0]
        self.test_e = self.config.get("test", [])[1]

    def mkdir_output_folder(self):
        logger.info(f"mkdir: {self.output_folder}")
        if os.path.isdir(self.output_folder):
            logger.info(f"out folder is exist: {self.output_folder}")
            self.output_folder_is_exist = True
        os.makedirs(self.output_folder, exist_ok=True)

    def get_output_folder(self):
        return self.output_folder

    def output_folder_is_exists(self):
        return self.output_folder_is_exist
    
    def get_total_file_name(self):
        return os.path.join(self.output_folder, "total_results.md")
    

    def modify_a_yaml(self, yaml_path):
        regex_pattern = r'(data_handler_config:\s*&data_handler_config\s*\n\s*start_time:\s*\d{4}-\d{2}-\d{2}\s*\n\s*end_time:\s*\d{4}-\d{2}-\d{2}\s*\n\s*fit_start_time:\s*\d{4}-\d{2}-\d{2}\s*\n\s*fit_end_time:\s*\d{4}-\d{2}-\d{2})'
        replacement = f"data_handler_config: &data_handler_config\n    start_time: {self.train_s}\n    end_time: {self.test_e}\n    fit_start_time: {self.train_s}\n    fit_end_time: {self.train_e}"
        replace_in_file(yaml_path, regex_pattern, replacement)

        regex_pattern = r'(backtest:\s*\n\s*start_time:\s*\d{4}-\d{2}-\d{2}\s*\n\s*end_time:\s*\d{4}-\d{2}-\d{2})'
        replacement = f"""backtest:
        start_time: {self.test_s}
        end_time: {self.test_e}"""  # 替换为新的配置内容

        replace_in_file(yaml_path, regex_pattern, replacement)


        regex_pattern = r'(segments:\s*\n\s*train:\s*\[\d{4}-\d{2}-\d{2},\s*\d{4}-\d{2}-\d{2}\]\s*\n\s*valid:\s*\[\d{4}-\d{2}-\d{2},\s*\d{4}-\d{2}-\d{2}\]\s*\n\s*test:\s*\[\d{4}-\d{2}-\d{2},\s*\d{4}-\d{2}-\d{2}\])'
        replacement = f"""segments:
                train: [{self.train_s}, {self.train_e}]
                valid: [{self.valid_s}, {self.valid_e}]
                test: [{self.test_s}, {self.test_e}]"""  # 替换为新的配置内容
        replace_in_file(yaml_path, regex_pattern, replacement)

        logger.info(f"modify yaml: {yaml_path}")

    def get_yamls_list(self):
        ret = []
        for item in self.config.get("qlib_yamls", []):
            if "#" in item:
                continue
            source = os.path.join(self.config["qlib_path"], item)
            dest = os.path.join(self.output_folder, os.path.basename(item))
            shutil.copyfile(source, dest)
            ret.append(dest)
        return ret

    def modify_all_yamls(self):
        for item in self.get_yamls_list():
            self.modify_a_yaml(item)

    def get_yaml_name(self, yaml):
        return os.path.basename(yaml).replace(".yaml", "")

    def get_qrun_cmd_list(self):
        ret = []
        for item in self.get_yamls_list():
            ret.append(f"qrun -e {self.get_yaml_name(item)}  -u {self.get_output_folder()} {item}")
        self.modify_all_yamls()
        return ret


if __name__ == "__main__":
    cl = ConfigLoader()
    cl.mkdir_output_folder()
    print(cl.get_output_folder())
    print(cl.get_yamls_list())
    print(cl.get_qrun_cmd_list())
    cl.modify_all_yamls()