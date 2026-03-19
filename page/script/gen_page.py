#!/usr/bin/env python3
"""
扫描 qlib_score_csv 子目录，生成 VitePress 静态页面。
所有 CSV 转为 Markdown 表格，MD 文件直接引用。
"""
import csv
import json
import os
import re
import shutil
from pathlib import Path

# 路径配置：page/script/gen_page.py -> 项目根目录
PAGE_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT = PAGE_ROOT.parent
DATA_DIR = PROJECT_ROOT / 'qlib_score_csv'
DOCS_DIR = PAGE_ROOT / 'docs'
BACKTEST_DIR = PROJECT_ROOT / 'backtest_csv'


def csv_to_markdown_table(csv_path: Path) -> str:
    """将 CSV 转为 Markdown 表格"""
    with open(csv_path, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return ''
    lines = []
    # 表头
    lines.append('| ' + ' | '.join(rows[0]) + ' |')
    lines.append('| ' + ' | '.join('---' for _ in rows[0]) + ' |')
    for row in rows[1:]:
        # 补齐列数
        while len(row) < len(rows[0]):
            row.append('')
        row = row[:len(rows[0])]
        lines.append('| ' + ' | '.join(str(c).replace('|', '\\|') for c in row) + ' |')
    return '\n'.join(lines)


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def sort_backtest_name(stem: str):
    """
    排序规则:
    1) 先 ret，再 filter_ret
    2) 同类型按 topN 从小到大
    3) 不匹配规则的文件放末尾并按名称排序
    """
    m = re.match(r'^(\d+)_(ret|filter_ret)$', stem)
    if not m:
        return (2, float('inf'), stem)
    topn = int(m.group(1))
    t = 0 if m.group(2) == 'ret' else 1
    return (t, topn, stem)


def format_backtest_heading(stem: str) -> str:
    """将文件 stem 转成友好的中文标题，如 Top10策略 ret。"""
    m = re.match(r'^(\d+)_(ret|filter_ret)$', stem)
    if not m:
        return stem
    topn, typ = m.group(1), m.group(2)
    return f'Top{topn}策略 {typ}'


def sync_backtest_csv_to_public() -> list[str]:
    """同步项目根目录 backtest_csv 到 docs/public/backtest_csv，并生成 index.json 清单。"""
    src_dir = BACKTEST_DIR
    dst_dir = DOCS_DIR / 'public' / 'backtest_csv'
    ensure_dir(dst_dir)

    # 清理旧 csv，避免历史脏文件残留
    for old_csv in dst_dir.glob('*.csv'):
        old_csv.unlink()

    if not src_dir.exists() or not src_dir.is_dir():
        (dst_dir / 'index.json').write_text(json.dumps([], ensure_ascii=False, indent=2), encoding='utf-8')
        return []

    files = [p for p in src_dir.iterdir() if p.is_file() and p.suffix == '.csv']
    files = sorted(files, key=lambda p: sort_backtest_name(p.stem))
    names = []
    for f in files:
        shutil.copy2(f, dst_dir / f.name)
        names.append(f.name)

    (dst_dir / 'index.json').write_text(json.dumps(names, ensure_ascii=False, indent=2), encoding='utf-8')
    return names


def generate_nav_curve_md(backtest_files: list[str]) -> None:
    """根据 backtest csv 清单自动生成 nav_curve.md，保证右侧目录可跳转。"""
    out = DOCS_DIR / 'pages' / 'mahoupao' / 'nav_curve.md'
    ensure_dir(out.parent)

    lines = [
        '# 净值曲线（Lightweight Charts）\n\n',
        '该页面使用 `Lightweight Charts` 绘制回测策略净值曲线，并与 `CSI300` 同图对比。  \n',
        '数据来源为项目根目录的 `backtest_csv/*.csv`，构建时会自动同步到站点的 `/backtest_csv/` 目录。\n\n',
        '## 文件约定\n\n',
        '- 文件名：`<topN>_<type>.csv`，例如 `10_ret.csv`、`20_filter_ret.csv`\n',
        '- 关键字段：`date`、`strategy_equity`、`csi300_equity`\n',
        '- 排序规则：先 `ret`，后 `filter_ret`；组内按 `topN` 从小到大\n\n',
    ]

    strategy_stems = [f[:-4] for f in backtest_files if f.endswith('.csv')]
    if not strategy_stems:
        lines.append('> 当前未检测到 backtest csv 文件。\n')
    else:
        for name in strategy_stems:
            lines.append(f'## {format_backtest_heading(name)}\n\n')
            lines.append(f'<NavCurveChart strategy="{name}" />\n\n')

    out.write_text(''.join(lines), encoding='utf-8')


def generate_pages() -> None:
    """扫描并生成所有页面"""
    if not DATA_DIR.exists():
        print(f'错误: 数据目录不存在 {DATA_DIR}')
        return

    # 清空 docs（保留 .vitepress、pages 和 public 用户资源）
    ensure_dir(DOCS_DIR)
    preserve = {'.vitepress', 'pages', 'public'}
    for p in DOCS_DIR.iterdir():
        if p.name in preserve:
            continue
        if p.is_dir():
            import shutil
            shutil.rmtree(p)
        else:
            p.unlink()

    sidebar_items = []
    subdirs = sorted([d for d in DATA_DIR.iterdir() if d.is_dir()], reverse=True)
    limit = os.environ.get('GEN_PAGE_LIMIT')
    if limit:
        subdirs = subdirs[: int(limit)]
        print(f'[CI] 限制展示最近 {limit} 个子目录')

    # 根 index
    index_lines = ['# qlib csi300 score\n', '点击下方或左侧查看打分预测。\n\n', '必看 [数据使用说明](https://touhoufan2024.github.io/qlibAssistant/pages/about/)\n\n', '必看 [复盘统计](https://touhoufan2024.github.io/qlibAssistant/pages/mahoupao/)\n\n']
    if (DATA_DIR / 'index.md').exists():
        index_lines.append((DATA_DIR / 'index.md').read_text(encoding='utf-8', errors='ignore'))
    index_lines.append('\n## 子目录列表\n')
    for d in subdirs:
        name = d.name
        link = f'/score/{name}/'
        index_lines.append(f'- [{name}]({link})\n')
        sidebar_items.append({
            'text': name,
            'link': f'/score/{name}/',
        })

    (DOCS_DIR / 'index.md').write_text(''.join(index_lines), encoding='utf-8')

    # 每个子目录
    for subdir in subdirs:
        rel = f'score/{subdir.name}'
        out_dir = DOCS_DIR / rel
        ensure_dir(out_dir)

        files = sorted(subdir.iterdir())
        md_files = [f for f in files if f.suffix == '.md']
        csv_files = [f for f in files if f.suffix == '.csv']

        # 子目录 index 先占位，生成页面后再写（确保与 page_content 一致）

        # 收集所有要生成的页面（MD 与 CSV 可能同名如 total）
        page_content: dict[str, list[str]] = {}  # base_name -> [sections]

        for f in md_files:
            content = f.read_text(encoding='utf-8', errors='ignore')
            if f.stem not in page_content:
                page_content[f.stem] = []
            page_content[f.stem].append(f'# {f.stem}\n\n{content}')

        for f in csv_files:
            table = csv_to_markdown_table(f)
            section = f'# {f.name}\n\n{table}'
            if f.stem not in page_content:
                page_content[f.stem] = []
            page_content[f.stem].append(section)

        for base_name, sections in page_content.items():
            out_path = out_dir / f'{base_name}.md'
            out_path.write_text('\n\n---\n\n'.join(sections), encoding='utf-8')

        # 子目录 index（按 base_name 排序）
        sub_index = [f'# {subdir.name}\n\n']
        for base_name in sorted(page_content.keys()):
            sub_index.append(f'- [{base_name}](/{rel}/{base_name})\n')
        (out_dir / 'index.md').write_text(''.join(sub_index), encoding='utf-8')

    # 同步回测 csv 到 public，供前端绘图，并生成马后炮净值页面
    backtest_files = sync_backtest_csv_to_public()
    generate_nav_curve_md(backtest_files)
    # 自动生成 pages 子页面链接和侧边栏（用户只需增删 md 文件）
    generate_pages_auto()

    # 更新 vitepress 侧边栏（数据目录）
    update_sidebar(sidebar_items)
    print(f'生成完成: {DOCS_DIR}')


# pages 下各文件夹的显示名称（与 nav 一致）
PAGES_TITLES: dict[str, str] = {
    'about': '帮助',
    'docs': '文档',
    'essays': '随笔',
    'mahoupao': '马后炮',
}


def _get_md_title(md_path: Path) -> str:
    """从 md 文件第一行 # 标题 提取显示名，否则用文件名"""
    try:
        text = md_path.read_text(encoding='utf-8', errors='ignore').strip()
        for line in text.split('\n')[:5]:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
    except Exception:
        pass
    return md_path.stem


def generate_pages_auto() -> None:
    """
    扫描 pages 下各子目录的 .md 文件，自动生成侧边栏配置。
    用户只需增删 md 文件，运行 gen 后侧边栏自动更新。
    """
    pages_dir = DOCS_DIR / 'pages'
    if not pages_dir.exists():
        return

    pages_sidebar: dict[str, list[dict[str, str]]] = {}

    for subdir in sorted(pages_dir.iterdir()):
        if not subdir.is_dir():
            continue
        subdir_name = subdir.name
        title = PAGES_TITLES.get(subdir_name, subdir_name)

        md_files = [
            f for f in subdir.iterdir()
            if f.is_file() and f.suffix == '.md' and f.name != 'index.md'
        ]
        md_files = sorted(md_files, key=lambda x: x.stem)

        # 只生成侧边栏，不修改 index.md 正文
        rel_path = f'/pages/{subdir_name}'
        sidebar_items = [
            {'text': title, 'link': f'{rel_path}/'},
        ]
        for f in md_files:
            display = _get_md_title(f)
            sidebar_items.append({'text': display, 'link': f'{rel_path}/{f.stem}'})

        # GitHub Pages 部署时 route 含 base，需两种 key 以兼容 dev 与 prod
        pages_sidebar[f'{rel_path}/'] = sidebar_items
        pages_sidebar[f'/qlibAssistant{rel_path}/'] = sidebar_items

    # 写入 sidebar-pages.generated.ts
    _write_sidebar_pages(pages_sidebar)


def _write_sidebar_pages(pages_sidebar: dict[str, list[dict[str, str]]]) -> None:
    """生成 .vitepress/sidebar-pages.generated.ts"""
    out = DOCS_DIR / '.vitepress' / 'sidebar-pages.generated.ts'
    lines = ["/** 由 gen_page.py 自动生成，请勿手动修改 */\n", "export const pagesSidebar = {\n"]
    for path, items in pages_sidebar.items():
        lines.append(f"  '{path}': [")
        for it in items:
            t = it['text'].replace("'", "\\'").replace('\\', '\\\\')
            lines.append(f"    {{ text: '{t}', link: '{it['link']}' }},")
        lines.append('  ],')
    lines.append('}\n')
    out.write_text('\n'.join(lines), encoding='utf-8')


def update_sidebar(items: list) -> None:
    """更新 vitepress 配置中的 sidebar（当 sidebar 为 false 时跳过）"""
    config_path = DOCS_DIR / '.vitepress' / 'config.ts'
    if not config_path.exists():
        return
    content = config_path.read_text(encoding='utf-8')
    if 'sidebar: false' in content:
        return

    def esc(s: str) -> str:
        return s.replace("'", "\\'").replace('\\', '\\\\')
    items_str = ',\n      '.join(
        f"{{ text: '{esc(i['text'])}', link: '{i['link']}' }}" for i in items
    )
    new_items = f"items: [{items_str}]"
    # 使用正则替换，兼容：1) 占位符 items: []  2) 已被替换过的旧 items: [...]
    pattern = r"items:\s*\[[\s\S]*?\]"
    new_content = re.sub(pattern, new_items, content, count=1)
    config_path.write_text(new_content, encoding='utf-8')


if __name__ == '__main__':
    generate_pages()
