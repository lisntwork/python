#!/usr/bin/env python
# -*-coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json

"""
    爬取网页
"""
def obtain_html(url):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data,'lxml')
    return soup


"""
    解析网页
"""
def pares_page(soup):
    message = soup.select('.movie-list dd')
    movie_list = []
    sum_movie = []
    for megs in message:
        imgs_link = megs.select('div.movie-item a div.movie-poster img')[1]
        ln = imgs_link.get('data-src')
        if ln:
            link = ln
            #print(link)
        movie_name = megs.select('div.channel-detail.movie-item-title a')[0]
        name = movie_name.string
        # print(name)
        score = megs.select('div.channel-detail.channel-detail-orange')[0]
        integer = score.select('i.integer')
        doubles = score.select('i.fraction')
        if integer and doubles:
            assess = integer[0].string + doubles[0].string
            # print(assess)
        else:
            assess = "暂无评分"
            #print(assess)
        movie_dict = {"movie_name":name,"movie_score":assess,"imgs_link":ln}
        #print(movie_dict)
        movie_list.append(movie_dict)
    return movie_list


"""
    存入文件
"""
def spider(page):
    message = []
    for i in range(page):
        url = ("https://maoyan.com/films?showType=3&offset=%s" %(i*30))
        response = obtain_html(url)
        movies = pares_page(response)
        message.append(movies)
    f = open('movie.json', 'w', encoding='utf-8')
    data = json.dumps(message)
    f.write(data)
    f.close()

if __name__ == "__main__":
    spider(6)


"""
    输出内容
"""
with open('movie.json','r',encoding='utf-8') as f:
    data = f.read()
    mv = json.loads(data)
    for M in mv:
        for m in M:
            print('='*160)
            print(m)


