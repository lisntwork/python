#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    爬取网站 http://www.allitebooks.com/page/1  书籍信息：书名，作者，简介，图片
"""
import requests
from lxml import etree
import csv

class BookSpider(object):
    def __init__(self):
        self.url = "http://www.allitebooks.com/page/{}"
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        self.book_list = []

    #访问页面的所有url
    def get_url_list(self,page):
        """
        :param page: 爬取的页数
        :return: 爬取页数的url列表
        """
        url_list = []
        for i in range(1,page):
            url_list.append(self.url.format(i))
        if url_list:
            return url_list
        else:
            return None

    #获取响应数据
    def get_html(self,url):
        """
        :param url: 爬取页面的url
        :return: 爬取页面的html
        """
        response = requests.get(url,headers=self.headers)
        if response.status_code == 200:
             return response.content.decode()
        else:
             return None

    #xpath解析获取书籍信息
    def parse_html(self,response):
        """
        :param self: 爬取的所有book信息以字典的格式存入列表
        :param response: 页面的html信息
        :return: None
        """
        html = etree.HTML(response)
        # 获取每页的所有书籍book
        page_book_list = html.xpath('//div[@class="main-content-inner clearfix"]/article')
        for book in page_book_list:
            book_dict ={}
            # 获取书名
            book_dict["book_title"] = book_title = book.xpath('.//div[@class="entry-body"]/ header[@class="entry-header"]/h2/a/text()')[0]
            # 获取作者
            book_dict["book_author"] = "、".join(book.xpath('.//div[@class="entry-body"]/header[@class="entry-header"]/div[@class="entry-meta"]/span/h5/a/text()'))
            # 获取简介
            book_dict["book_introduction"] = book.xpath('.//div[@class="entry-body"]/div[@class="entry-summary"]/p/text()')[0]
            # 获取书籍图片
            book_dict["book_img"] = book.xpath('div[@class="entry-thumbnail hover-thumb"]/a/img/@src')[0]
            self.book_list.append(book_dict)

    #爬取的所有book信息写入csv格式文件
    def save_file(self):
        f = open("book.csv",'a+',encoding='utf-8-sig',newline='')
        csv_write = csv.writer(f)
        sheet_title = self.book_list[0].keys()
        csv_write.writerow(sheet_title)
        for book_dict in self.book_list:
            sheet_data = book_dict.values()
            csv_write.writerow(sheet_data)
        f.close()

    #启动函数
    def run(self):
        #传入爬取页面数 20
        urls = self.get_url_list(20)
        for url in urls:
            html = self.get_html(url)
            self.parse_html(html)
        self.save_file()

BookSpider().run()
