#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
    爬取网易云音乐歌单信息 url:https://music.163.com/#/discover/playlist/?order=hot&cat=华语&limit=35&offset=0
"""
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'user-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }

"""
    获取指定范围歌单页详细信息
"""
def songlist_detail_message(links_list):
    #创建csv格式文件
    csv_file=open('music_detail.csv','a+',encoding='utf-8-sig',newline='')
    fildenames = ['title','author','create','tag','fav','share','cmmt','intr']
    writer = csv.DictWriter(csv_file,fieldnames=fildenames)
    writer.writeheader()
    #循环遍历每个链接，抓取数据并写入文件
    for link in links_list:
        url = link
        response = requests.get(url).text
        soup = BeautifulSoup(response,'html.parser')

        #歌单标题
        title = soup.select('div.cnt div.cntc div.hd.f-cb div.tit h2.f-ff2.f-brk')[0].text
        # print(title)

        #歌单作者
        author = soup.select('div.cnt div.cntc div.user.f-cb span.name a.s-fc7')[0].text
        # print(author)

        #歌单发布时间
        create = soup.select('div.cnt div.cntc div.user.f-cb span.time.s-fc4')[0].text.replace('创建','')
        # print(create)

        #歌单标签
        tags = soup.select(' div.cnt div.cntc div.tags.f-cb a.u-tag i')
        list_tags = []
        for tag in tags:
            list_tags.append(tag.text)
        tag = ' '.join(list_tags)
        # print(tag)

        #歌单收藏数
        fav = soup.select('div.btns.f-cb a.u-btni.u-btni-fav i')[0].text.replace('(','').replace(')','')
        # print(fav)

        #歌单分享数
        share = soup.select('div.cnt div.cntc div#content-operation a.u-btni.u-btni-share i')[0].text.replace('(','').replace(')','')
        # print(share)

        #歌单评论数
        cmmt = soup.select('div.cnt div.cntc div#content-operation a.u-btni.u-btni-cmmt i span#cnt_comment_count')[0].text
        # print(cmmt)

        #歌单介绍
        if soup.select('div.cnt div.cntc p#album-desc-more'):
            intr = soup.select('div.cnt div.cntc p#album-desc-more')[0].text.replace('华语 / 流行 / 民谣 / 以丧治丧','').replace('介绍：','').replace('-','').replace('\n\n',' ').replace('，',' ')
        else:
            intr ="NO Introduction"
        # print(intr)
        music_dict = {'title':title,
                      'author': author,
                     'create':create,
                      'tag':tag,
                      'fav':fav,
                      'share':share,
                      'cmmt':cmmt,
                      'intr':intr
                     }
        writer.writerow(music_dict)
    csv_file.close()

"""
    获取指定范围页面歌单信息
"""
def songlist_index_message(page):
    csv_file = open('music_index.csv', 'a+', encoding='utf-8-sig', newline='')
    filednames = ['title', 'author', 'play', 'link']
    writer = csv.DictWriter(csv_file, fieldnames=filednames)
    writer.writeheader()
    # 收集歌单详细信息url的列表
    links_list = []
    #遍历没指定范围的歌单页数
    for i in range(0,page,35):
        url = ('https://music.163.com/#/discover/playlist/?order=hot&cat=华语&limit=35&offset=%s' %(i))
        brower = webdriver.Chrome()
        brower.get(url)
        brower.switch_to.frame("contentFrame")
        music_list = brower.find_elements_by_xpath("//ul[@id='m-pl-container']/li")
        #获取每一页歌单简要信息
        for music in music_list:
            #获取歌单标题
            title = music.find_element_by_css_selector('p.dec a.tit.f-thide.s-fc0').text
            #获取歌单详细链接
            link = music.find_element_by_css_selector('div.u-cover.u-cover-1 a.msk').get_attribute('href')
            links_list.append(link)
            #获取歌单作者
            author = music.find_element_by_css_selector('p a.nm.nm-icn.f-thide.s-fc3').text
            #获取歌单点击量
            play = music.find_element_by_css_selector('div.u-cover.u-cover-1 div.bottom span.nb').text
            # print(play)

            music_dict = {
                'title':title,
                'author':author,
                'play':play,
                'link':link
                }
            writer.writerow(music_dict)
    csv_file.close()
    print(len(links_list))
    return links_list

if __name__ == '__main__':
    #传入抓取歌单页面数 3
    links_list = songlist_index_message(3 * 35)
    songlist_detail_message(links_list)







