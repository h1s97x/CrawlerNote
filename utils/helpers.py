"""
爬虫工具函数集合
"""
import time
import random
from fake_useragent import UserAgent

def get_random_headers():
    """生成随机请求头"""
    ua = UserAgent()
    return {
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }

def random_delay(min_seconds=1, max_seconds=3):
    """随机延迟，避免被封"""
    time.sleep(random.uniform(min_seconds, max_seconds))

def save_to_csv(data, filename):
    """保存数据到 CSV"""
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"数据已保存到 {filename}")
