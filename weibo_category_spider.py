#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    基于AjaX爬取新浪微博搞笑榜  “https://weibo.com/?category=10011”
"""
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
import json

def spider(page):
    headers = {
        'Host': 'weibo.com',
        'Referer': 'https://weibo.com/?category=10011',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    params ={
        'ajwvr': 0,
        'category': 10011,
        'page': page,
        'lefnav': 0
    }

    url = 'https://weibo.com/a/aj/transform/loadingmoreunlogin?' + urlencode(params)

    response = requests.get(url,headers = headers)
    messages = response.json().get('data')
    soup = BeautifulSoup(messages,'lxml')
    rest = soup.select('ul')
    return rest

def parse_a(list_a):
    sum_list = []
    imgs_link = []
    for list in list_a:
        links = list.select('div.list_nod.clearfix div.pic.W_piccut_v')
        for link in links:
            img = link.select('img')[0].get('src')
            imgs_link.append(img)
        # print(imgs_link)

        """
        获取每隔页面所有list_a标题title
        """
        title = list.select('h3.list_title_s.W_autocut div')[0].get_text()
        # print(title)
        """
        获取每隔页面所有list_a作者author
        """
        author = list.select('div.subinfo_box.clearfix span.subinfo.S_txt2')[0].string
        # print(author)
        """
        获取每隔页面所有list_a作者author
        """
        date = list.select('div.subinfo_box.clearfix span.subinfo.S_txt2')[1].get_text()
        # print(date)
        """
            获取每个页面所有list_a点赞
        """
        like = list.select('div.subinfo_box.clearfix span.subinfo_rgt.S_txt2 em')[1].string
        # print(like)
        """
            获取每个页面所有list_a点评论
        """
        comment = list.select('div.subinfo_box.clearfix span.subinfo_rgt.S_txt2 em')[3].string
        # print(comment)
        """
            获取每个页面所有list_a分享数
        """
        share = list.select('div.subinfo_box.clearfix span.subinfo_rgt.S_txt2 em')[5].string
        # print(share)
        list_a_dict = {"title": title,
                       "author": author,
                       "date": date,
                       "like": like,
                       "comment": comment,
                       "share": share,
                       "img_link": imgs_link
                       }
        sum_list.append(list_a_dict)
    return sum_list

def parse_b(list_b):
    sum_list = []
    for list in list_b:
        """
            获取每个页面所有list_b的图片链接imgs_link
        """
        imgs_link = list.select('div img')[0].get('src')
        # print(imgs_link)

        """
            获取每个页面所有list_b的标题title
        """
        title = list.select('div.list_des h3')[0].get_text()
        # print(title)

        """
           获取每隔页面所有list_b的作者author
        """
        author = list.select('div.list_des div.subinfo_box.clearfix span.subinfo.S_txt2')[0].string
        # print(author)

        """
            获取每隔页面所有list_b的发布时间date
        """
        date = list.select('div.list_des div.subinfo_box.clearfix span.subinfo.S_txt2')[1].string
        # print(date)
        """
            获取每个页面所有list_a点赞
        """
        like = list.select('div.list_des div.subinfo_box.clearfix span.subinfo_rgt.S_txt2 em')[1].string
        # print(like)

        """
            获取每个页面所有list_b评论数
        """
        comment = list.select('div.list_des div.subinfo_box.clearfix span.subinfo_rgt.S_txt2 em')[3].string
        # print(comment)
        """
            获取每个页面所有list_b分享数
        """
        share = list.select('div.list_des div.subinfo_box.clearfix span.subinfo_rgt.S_txt2 em')[5].string
        # print(share)
        list_b_dict = {"title": title,
                       "author": author,
                       "date": date,
                       "like": like,
                       "comment": comment,
                       "share": share,
                       "img_link": imgs_link
                       }
        sum_list.append(list_b_dict)
    return sum_list

def parse_c(list_c):
    sum_list = []
    for list in list_c:
        """
            获取每个页面所有list_c的图片链接imgs_link
        """
        imgs_link = list.div.div.img.get('src')
        # print(imgs_link)
        """
            获取每个页面所有list_c的标题title
        """
        title = list.select('div.list_des h3')[0].get_text()
        # print(title)

        """
            获取每隔页面所有list_c的作者author
        """
        author = list.select('div.list_des div.subinfo_box.clearfix span.subinfo.S_txt2')[0].string
        # print(author)

        """
            获取每隔页面所有list_c的发布时间date
        """
        date = list.select('div.list_des div.subinfo_box.clearfix span.subinfo.S_txt2')[1].string
        # print(date)
        """
            获取每个页面所有list_c点赞
         """
        like = list.select('div.list_des div.subinfo_box.clearfix.subinfo_box_btm span.subinfo_rgt.S_txt2 em')[1].string
        # print(like)

        """
             获取每个页面所有list_b评论数
        """
        comment = list.select('div.list_des div.subinfo_box.clearfix.subinfo_box_btm span.subinfo_rgt.S_txt2 em')[
            3].string
        # print(comment)
        """
            获取每个页面所有list_b分享数
        """
        share = list.select('div.list_des div.subinfo_box.clearfix.subinfo_box_btm span.subinfo_rgt.S_txt2 em')[
            5].string
        # print(share)

        list_c_dict = {"title": title,
                       "author": author,
                       "date": date,
                       "like": like,
                       "comment": comment,
                       "share": share,
                       "img_link": imgs_link
                       }
        sum_list.append(list_c_dict)
    return sum_list

def result(pages):
    data = []
    for page in range(pages):
        megs = spider(page)
        #获取每一页所有的list_a信息
        list_a = megs[0].select('div.UG_list_a')
        if len(list_a):
            # print("=================A====================")
            a = parse_a(list_a)
            data.append(a)
            # print(a)
        # 获取每一页所有的list_b信息
        list_b = megs[0].select('div.UG_list_b')
        if len(list_b):
            # print("=================B====================")
            b = parse_b(list_b)
            data.append(b)
            # print(b)
        # 获取每一页所有的list_c信息
        list_c = megs[0].select('div.UG_list_v2.clearfix')
        if list_c:
            # print("=================C====================")
            c = parse_c(list_c)
            # print(c)
            data.append(c)
    return data

def write_file(db):
    db = json.dumps(db)
    with open('weibo.json','w',encoding='utf-8') as f:
        f.write(db)

 if __name__ == '__main__':
      # 传入爬取的页数并将爬取的内容写入文件
      db = result(20)
      write_file(db)


"""
    读取文件内容
"""

"""
with open('weibo.json','r',encoding='utf-8') as f:
    data = f.read()
    print(json.loads(data))

"""
