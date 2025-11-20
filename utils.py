import tomllib
import os

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

if __name__ == "__main__":
    config = get_config()
    print(config)