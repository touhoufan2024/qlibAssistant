import tomllib
import os
from datetime import datetime
from loguru import logger

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
        logger.info(f"mkdir: {self.output_folder}")
        if os.path.isdir(self.output_folder):
            logger.info(f"out folder is exist: {self.output_folder}")
            self.output_folder_is_exist = True
        os.makedirs(self.output_folder, exist_ok=True)

    def get_output_folder(self):
        return self.output_folder

    def output_folder_is_exists(self):
        return self.output_folder_is_exist
    
    def get_yamls_list(self):
        ret = []
        for item in self.config.get("qlib_yamls", []):
            ret.append(os.path.join(self.config["qlib_path"], item))
        return ret

    def get_yaml_name(self, yaml):
        return os.path.basename(yaml).replace(".yaml", "")

    def get_qrun_cmd_list(self):
        ret = []
        for item in self.get_yamls_list():
            ret.append(f"qrun -e {self.get_yaml_name(item)}  -u {self.get_output_folder()} {item}")
        return ret


if __name__ == "__main__":
    cl = ConfigLoader()
    print(cl.get_output_folder())
    print(cl.get_yamls_list())
    print(cl.get_qrun_cmd_list())