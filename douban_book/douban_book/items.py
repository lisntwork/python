# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class DoubanBookItem(scrapy.Item):

    name = scrapy.Field()
    price = scrapy.Field()
    publisher = scrapy.Field()
    ratings = scrapy.Field()
    edition_year = scrapy.Field()
    author = scrapy.Field()