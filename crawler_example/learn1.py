import requests_
import json


# 获取网址源码（无用）
def get_html_():
    url = 'https://movie.douban.com/?_t_t_t=0.22263539559207857'

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

    html = requests_.get(url, headers = headers).content.decode()

    print(html)

def get_content():
    url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

    html = requests_.get(url, headers=headers).content.decode()

    # print(html)

    dic = json.loads(html)

    print(type(dic))

get_content()

