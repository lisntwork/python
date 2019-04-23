#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup

"""
    爬取笑话网信息 url：http://www.duodia.com/daxuexiaohua/list_1.html
"""

def spider_messages(page):
    for i in range(1,page):
        url = ('http://www.duodia.com/daxuexiaohua/list_%s.html' %(i))
        response = requests.get(url).text
        message = BeautifulSoup(response,'lxml')
        datas = message.select('article')
        for data in datas:
            descr = data.select('div.card-bg a.card-title h3')[0].string
            # print(descr)
            link = data.select('div.card-bg a.thumbnail-container img')[0].get('src')
            # print(link)
            date = data.select('div.card-bg div.card-meta time.meta.time')[0].string.replace('\t','').replace('\n','').replace('\r','')
            # print(date)
            click = data.select('div.card-bg div.card-meta span.meta.play')[0].get_text().replace('\t','').replace('\n','').replace('\r','')
            # print(click)
            mges = {'descr':descr,
                    'link':link,
                    'date':date,
                    'click':click
                    }
            print(mges)

if __name__ == '__main__':
    """
        传入爬取的页码参数
    """
    spider_messages(5)


