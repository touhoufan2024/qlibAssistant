import tomllib
import os
from datetime import datetime

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
        os.makedirs(self.output_folder, exist_ok=True)

    def get_output_folder(self):
        return self.output_folder


if __name__ == "__main__":
    cl = ConfigLoader()
    print(cl.config)