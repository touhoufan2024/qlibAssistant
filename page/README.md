# qlib csi300 score 静态文档站

基于 VitePress 的静态网站，展示 `qlib_score_csv` 目录下的 CSV 和 MD 文件。

## 目录结构

```
page/
├── docs/                 # VitePress 文档（部分由 gen_page 生成）
│   ├── .vitepress/       # 配置与主题
│   ├── index.md          # 首页
│   ├── score/            # 各 selection 子目录
│   └── pages/            # 用户页面（保留）
│       ├── docs.md       # 文档（单页，类似帮助）
│       ├── essays/       # 随笔：新建 .md 后运行 gen 自动生成索引
│       └── about.md      # 关于页
├── script/
│   └── gen_page.py       # 扫描并生成页面
├── package.json
└── README.md
```

## 随笔

在 `docs/pages/essays/` 下新建 `.md` 文件，运行 `npm run gen` 后会自动出现在对应列表中。文档（`docs.md`）为单页，与帮助页类似，直接编辑即可。

## 使用

```bash
# 1. 安装依赖
cd page && npm install

# 2. 生成页面（扫描 ../qlib_score_csv）
npm run gen

# 3. 本地开发
npm run docs:dev

# 4. 构建静态站点
npm run docs:build
```

构建产物在 `docs/.vitepress/dist/`。
