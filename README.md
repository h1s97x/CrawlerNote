# Jupyter Notebook 爬虫演示项目

本项目使用 Jupyter Notebook 演示各种网页爬虫技术和工具。

## 项目结构

```
.
├── notebooks/              # Jupyter Notebook 教程
│   ├── 01_basic_scraping.ipynb          # 基础爬虫
│   ├── 02_dynamic_content.ipynb         # 动态内容抓取
│   ├── 03_api_scraping.ipynb            # API 数据获取
│   ├── 04_data_cleaning.ipynb           # 数据清洗
│   ├── 05_advanced_techniques.ipynb     # 高级技巧
│   └── 06_law_document_scraper.ipynb    # 法律文书爬虫
├── data/                   # 存放抓取的数据
├── utils/                  # 工具函数
│   └── helpers.py
├── docs/                   # 文档
│   └── jupyter-notebook-crawler.md
├── requirements.txt        # 依赖列表
└── README.md              # 本文件
```

## 快速开始

### 1. 环境准备

创建虚拟环境：

```bash
python -m venv venv
```

激活虚拟环境：

- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 启动 Jupyter Notebook

```bash
jupyter notebook
```

浏览器会自动打开 `http://localhost:8888`，然后进入 `notebooks/` 目录开始学习。

## 教程内容

### 01 - 基础爬虫
- HTTP 请求基础
- HTML 解析
- 使用 BeautifulSoup 提取数据
- 数据保存

### 02 - 动态内容抓取
- Selenium 基础
- 等待页面加载
- 处理 JavaScript 渲染的内容
- 分页和滚动加载

### 03 - API 数据获取
- REST API 调用
- JSON 数据处理
- 参数传递和认证
- 数据可视化

### 04 - 数据清洗
- 处理缺失值
- 数据类型转换
- 文本清洗
- 数据去重和验证

### 05 - 高级技巧
- 并发爬取
- 错误处理和重试
- 反爬虫应对
- 会话管理

### 06 - 法律文书爬虫
- 中国裁判文书网自动化爬取
- 自动登录和认证
- iframe 框架处理
- 高级检索和批量下载

## 技术栈

- **requests**: HTTP 请求
- **BeautifulSoup**: HTML 解析
- **Selenium**: 动态内容抓取
- **pandas**: 数据处理
- **matplotlib/seaborn**: 数据可视化
- **Jupyter**: 交互式开发环境

## 注意事项

1. 遵守网站的 robots.txt 规则
2. 合理设置请求频率，避免对目标网站造成压力
3. 尊重网站的服务条款
4. 不要爬取敏感或受版权保护的内容

## 学习路径

建议按照以下顺序学习：

1. 先阅读 `docs/jupyter-notebook-crawler.md` 了解基础概念
2. 按顺序完成 01-05 的 notebook 教程
3. 学习 06 法律文书爬虫的实战案例
4. 尝试修改代码，爬取自己感兴趣的网站
5. 结合实际项目需求，应用所学技术

## 常见问题

### Selenium 驱动问题

如果遇到 ChromeDriver 问题，可以：

```bash
pip install webdriver-manager
```

然后在代码中使用：

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
```

### 编码问题

保存 CSV 时使用 `encoding='utf-8-sig'` 避免中文乱码。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可

MIT License
