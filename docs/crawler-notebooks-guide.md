# Python 网络爬虫 Jupyter Notebook 教程

## 概述

本教程将 `Python3网络爬虫-源码` 文件夹中的爬虫代码转换为交互式 Jupyter Notebook 格式，便于学习和实践。

## 原始代码结构

原始代码按章节组织（C1-C12），包含以下内容：

- **C1**: Python 基础入门
- **C2**: HTML 基础
- **C3**: 文件操作和数据处理（文本、CSV、JSON、XML）
- **C4**: urllib 基础爬虫、日志记录
- **C5**: Scrapy 框架、代理获取
- **C6**: BeautifulSoup 解析（电影、贴吧、小说、彩票等）
- **C7-C9**: 高级爬虫技术
- **C10**: OCR 图像识别（pytesseract）
- **C11**: mitmproxy 代理抓包
- **C12**: 代理和 User-Agent 管理

## 转换后的 Notebook

### 已创建的 Notebook

1. **07_urllib_basic_crawler.ipynb** - urllib 基础爬虫
   - 基础网页连接
   - 添加请求头（User-Agent）
   - 使用代理
   - 正则表达式提取数据
   - 完整爬虫示例

2. **08_beautifulsoup_crawler.ipynb** - BeautifulSoup 网页解析
   - BeautifulSoup 基础
   - 查找元素方法（find, find_all, select）
   - 提取数据技巧
   - 实战：电影信息爬虫
   - 实战：贴吧内容爬虫
   - 常用技巧总结

3. **09_file_operations.ipynb** - 文件操作与数据处理
   - 文本文件读写
   - CSV 文件处理
   - JSON 数据处理
   - XML 数据处理
   - 日志记录
   - 综合示例：数据管道

4. **10_scrapy_framework.ipynb** - Scrapy 爬虫框架
   - Scrapy 简介和架构
   - 项目结构
   - Spider 编写
   - Item 定义
   - Pipeline 处理
   - 中间件使用
   - Settings 配置
   - CSS 和 XPath 选择器

## 使用方法

### 1. 安装依赖

```bash
# 基础依赖
pip install jupyter notebook

# 爬虫依赖
pip install requests beautifulsoup4 lxml scrapy

# 可选依赖
pip install selenium pytesseract pillow
```

### 2. 启动 Jupyter Notebook

```bash
cd notebooks
jupyter notebook
```

### 3. 学习路径

建议按以下顺序学习：

1. 先学习已有的基础教程（01-06）
2. 学习 urllib 基础爬虫（07）
3. 学习 BeautifulSoup 解析（08）
4. 学习文件操作（09）
5. 学习 Scrapy 框架（10）

## 原始代码示例

### C4 - urllib 基础爬虫

```python
# connBaidu.py - 连接百度
import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url, timeout=3)
result = response.read().decode('utf-8')

print(f"URL: {response.geturl()}")
print(f"状态码: {response.getcode()}")
```

### C6 - BeautifulSoup 电影爬虫

```python
# get2016movie.py - 爬取2016年电影
from bs4 import BeautifulSoup
import urllib.request

class MovieItem:
    movieName = None
    movieScore = None
    movieStarring = None

# 解析电影信息
soup = BeautifulSoup(htmlContent, 'lxml')
tags = soup.find_all('li', attrs={'media': re.compile(r'\d{5}')})
```

### C5 - Scrapy 代理爬虫

```python
# xiciSpider.py - 西刺代理爬虫
import scrapy

class ProxySpider(scrapy.Spider):
    name = 'xici'
    start_urls = ['http://www.xicidaili.com/']
    
    def parse(self, response):
        # 提取代理信息
        for tr in response.css('table tr'):
            yield {
                'ip': tr.css('td:nth-child(2)::text').get(),
                'port': tr.css('td:nth-child(3)::text').get()
            }
```

## 特色功能

### 1. 交互式学习
- 每个代码块可以独立运行
- 即时查看输出结果
- 方便修改和实验

### 2. 完整示例
- 基于原始代码改编
- 保留核心逻辑
- 添加详细注释

### 3. 实战项目
- 电影信息爬虫
- 贴吧内容爬虫
- 代理 IP 获取
- 数据清洗和存储

### 4. 最佳实践
- 异常处理
- 日志记录
- 数据验证
- 反爬虫策略

## 注意事项

### 法律和道德
- 遵守网站的 robots.txt 规则
- 不要过度爬取，避免对服务器造成压力
- 尊重网站的版权和用户隐私
- 仅用于学习和研究目的

### 技术建议
- 合理设置请求延迟
- 使用随机 User-Agent
- 处理异常情况
- 记录日志便于调试

### 反爬虫应对
- 使用代理 IP 池
- 模拟浏览器行为
- 处理验证码
- 分析网站的反爬虫机制

## 扩展学习

### 推荐资源
- Scrapy 官方文档: https://docs.scrapy.org/
- BeautifulSoup 文档: https://www.crummy.com/software/BeautifulSoup/
- Requests 文档: https://requests.readthedocs.io/

### 进阶主题
- Selenium 动态网页爬取
- Splash JavaScript 渲染
- 分布式爬虫
- 爬虫部署和监控

## 练习项目

1. **豆瓣电影 Top250**
   - 爬取电影信息
   - 保存为 CSV 和 JSON
   - 数据可视化

2. **新闻网站爬虫**
   - 爬取新闻标题和内容
   - 自动翻页
   - 定时更新

3. **电商价格监控**
   - 监控商品价格
   - 价格变动提醒
   - 历史价格分析

4. **招聘信息爬虫**
   - 爬取招聘网站
   - 职位信息分析
   - 薪资统计

## 贡献

欢迎提交问题和改进建议！

## 许可

本教程仅供学习使用，请遵守相关法律法规。
