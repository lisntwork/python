# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DangdangItem(scrapy.Item):
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_price = scrapy.Field()
    #书籍评论数
    book_star = scrapy.Field()
    #书籍出版时间
    published_time =scrapy.Field()
    #书籍出版社
    publish_house = scrapy.Field()


