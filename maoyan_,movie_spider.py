#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import etree
import csv

url = "https://maoyan.com/board/4?"

headers ={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }

params = {
    "offset":0
}

def get_html(page):
    """
    获取一页html页面
    :param page: 页数
    :return: 此页面的html
    """
    params["offset"] = page * 10
    try:
        response = requests.get(url=url,headers=headers,params=params)
        if response.status_code == 200:
            return response.content.decode()
        else:
            return -1
    except:
        return None

def parse_html(response):
    """
    使用xpath解析页面中的电影信息
    :param response: 页面的html
    :return: 每页电影信息列表
    """
    #构造xpath解析对象
    html = etree.HTML(response)
    results = html.xpath("//dd")
    if results:
        #每页电影信息放入该列表返回
        page_html_list= []
        #获取电影信息
        for result in results:
            movie_dict = {}
            #电影排名
            film_ranking = result.xpath('./i/text()')[0]
            movie_dict['film_ranking'] = film_ranking
            #电影名称
            film_name = result.xpath('.//a/text()')[3]
            movie_dict['film_name'] = film_name
            #电影主演
            film_starring = result.xpath('.//p[@class="star"]/text()')[0].replace('主演：','').strip()
            movie_dict['film_starring'] = film_starring
            #电影上映时间
            release_time =result.xpath('.//p[@class="releasetime"]/text()')[0].replace('上映时间：','')
            movie_dict['release_time'] = release_time
            #电影评分
            film_score = "".join(result.xpath('.//p[@class="score"]//text()'))
            movie_dict['film_score'] = film_score
            page_html_list.append(movie_dict)
        return page_html_list
    else:
        return None

def save_info(page_html_list):
    """
    电影信息保存至csv格式文件
    :param page_html_list: 每页所有电影信息列表
    :return: None
    """
    with open('top_film.csv','a',encoding='utf-8-sig',newline='') as f:
        csv_file = csv.writer(f)
        for film_dict in page_html_list:
            csv_file.writerow([film_dict['film_ranking'],film_dict['film_name'],film_dict['film_starring'],film_dict['release_time'],film_dict['film_score']])

if __name__ == '__main__':
    for page in range(10):
        response = get_html(page)
        page_html_list = parse_html(response)
        save_info(page_html_list)












