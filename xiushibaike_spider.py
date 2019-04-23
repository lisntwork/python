#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    爬取嗅事百科段子  url：https://www.qiushibaike.com/hot/page/1/
    爬取信息：文本，作者，评论数，好笑数
"""
import requests
from bs4 import BeautifulSoup
import json

def get_page(page):
    url = ('https://www.qiushibaike.com/hot/page/%s' %(page+1))
    response = requests.get(url).text
    soup = BeautifulSoup(response,'lxml')
    return soup

def parse_page(soup):
    """
        获取文本内容，得到一个列表
    """
    mesges = soup.select('div.article.block.untagged.mb15.typs_hot a.contentHerf div.content span')
    """
        获取文本作者，得到一个列表
    """
    authors = soup.select('div.article.block.untagged.mb15.typs_hot div.author.clearfix h2')
    """
        获取文本好笑数量，得到一个列表
    """
    funny = soup.select('div.article.block.untagged.mb15.typs_hot div.stats span.stats-vote i.number')
    """
        获取文本评论数量，得到一个列表
    """
    comments = soup.select('div.article.block.untagged.mb15.typs_hot div.stats span.stats-comments a.qiushi_comments i.number')
    """
            使用python内置函数zip，它可以将x个y维列表变成一个zip对象，还可以将这个对象变成一个元组或列表
    """
    merge = list(zip(mesges,authors,funny,comments))
    megs_list = []

    """
        遍历列表信息，生成对应的字典
    """
    for m in merge:
        megs_dict = {
            'text':m[0].get_text().replace('\n',''),
            'author':m[1].string.replace('\n',''),
            'funny':m[2].string,
            'comments':m[3].string
            }
        megs_list.append(megs_dict)
    """
        将每一页的每个段子信息以字典的形式存入列表，并返回每一页段子信息列表
    """
    return megs_list

def write_to_file(data):
    db = json.dumps(data)
    with open('xiushi.json','w',encoding='utf-8') as f:
        f.write(db)

def main(page):
    """
        将每一个页的段子信息列表存入一个大的列表，并返回
    """
    page_list = []
    for i in range(page):
        soup = get_page(i)
        megs = parse_page(soup)
        page_list.append(megs)
        write_to_file(page_list)


if __name__ == '__main__':
    """
        传入爬取的网页数量
    """
    main(9)

"""
with open('xiushi.json','r',encoding='utf-8') as f:
    db = f.read()
    data = json.loads(db)
    print(data)
    
"""

