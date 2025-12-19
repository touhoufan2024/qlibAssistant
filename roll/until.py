import subprocess

def run_command(command):
    """
    执行 CMD 命令并返回结果
    :param command: 字符串格式的命令
    :return: (状态码, 输出内容, 错误信息)
    """
    try:
        # shell=True 表示通过 shell 执行（可以使用 dir, copy 等内建命令）
        # capture_output=True 捕捉标准输出和错误
        # text=True 将输出结果转为字符串（自动处理换行）
        # encoding="utf-8" 指定编码，Windows 下如果乱码可以尝试改为 "gbk"
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            encoding="utf-8" 
        )
        
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)