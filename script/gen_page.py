import os
import shutil
import subprocess
from pathlib import Path

# --- 配置区 ---
DATA_DIR = './qlib_score_csv'    # 存放 CSV/TXT 的源目录
BUILD_DIR = './site_project'      # MkDocs 项目生成目录
SITE_NAME = "qlib csi300 score"

def setup_project():
    """初始化 MkDocs 项目结构并配置 yml"""
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(os.path.join(BUILD_DIR, "docs", "stylesheets"), exist_ok=True)

    # 这里的 use_directory_urls: false 解决了点击链接跳到“索引”页面的问题
    config = f"""
site_name: {SITE_NAME}
use_directory_urls: false  
theme:
  name: material
  language: zh
  features:
    - navigation.expand
    - navigation.sections
    - search.highlight
extra_css:
  - stylesheets/extra.css
plugins:
  - search
  - table-reader
"""
    with open(os.path.join(BUILD_DIR, "mkdocs.yml"), "w", encoding="utf-8") as f:
        f.write(config)

def create_custom_css():
    """创建自定义 CSS 让页面铺满并支持横向滚动"""
    css_path = os.path.join(BUILD_DIR, "docs", "stylesheets", "extra.css")
    css_content = """
/* 1. 强制页面宽度铺满 */
.md-grid {
    max-width: 98% !important;
}
.md-main__inner {
    max-width: 100% !important;
}

/* 2. 表格容器：允许横向滚动，不换行 */
.md-typeset table {
    display: block;
    overflow-x: auto;
    width: 100%;
    border-collapse: collapse;
}

/* 3. 单元格：保持列宽，防止文字挤压 */
.md-typeset td, .md-typeset th {
    min-width: 150px;    /* 每一列最小 150px */
    white-space: nowrap; /* 强制不换行 */
    padding: 12px;
}

/* 4. 固定第一列 (可选，滑动时 ID 列不动) */
.md-typeset th:first-child, 
.md-typeset td:first-child {
    position: sticky;
    left: 0;
    z-index: 1;
    background-color: #fff;
    border-right: 2px solid #eee;
}
"""
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)

def scan_and_generate():
    """遍历目录生成 Markdown"""
    source_root = Path(DATA_DIR).resolve()
    docs_root = Path(BUILD_DIR) / "docs"

    # 生成首页
    with open(docs_root / "index.md", "w", encoding="utf-8") as f:
        f.write(f"# 📂 根目录\n\n自动扫描完成。点击左侧查看数据。")

    for root, dirs, files in os.walk(source_root):
        rel_path = Path(root).relative_to(source_root)
        target_dir = docs_root / rel_path
        os.makedirs(target_dir, exist_ok=True)

        for filename in files:
            file_path = Path(root) / filename
            if filename.endswith(('.csv', '.txt')):
                md_filename = f"{filename}.md"
                with open(target_dir / md_filename, "w", encoding="utf-8") as f:
                    if filename.endswith('.csv'):
                        f.write(f"# 📊 {filename}\n\n")
                        # 使用插件读取完整 CSV
                        f.write(f"{{{{ read_csv('{file_path.as_posix()}') }}}}")
                    elif filename.endswith('.txt'):
                        f.write(f"# 📄 {filename}\n\n```text\n")
                        f.write(file_path.read_text(encoding='utf-8', errors='ignore'))
                        f.write("\n```")

def build_site():
    """构建静态网站"""
    print(f"🚀 开始构建...")
    result = subprocess.run(["mkdocs", "build"], cwd=BUILD_DIR)
    if result.returncode == 0:
        site_path = os.path.abspath(os.path.join(BUILD_DIR, 'site'))
        print(f"\n✨ 构建完成！")
        print(f"📂 静态网页目录: {site_path}")
        print(f"💡 本地直接打开: 双击 {site_path}/index.html")
        print(f"💡 WSL 预览命令: cd {BUILD_DIR}/site && python3 -m http.server 8080")

if __name__ == "__main__":
    setup_project()
    create_custom_css()
    scan_and_generate()
    build_site()