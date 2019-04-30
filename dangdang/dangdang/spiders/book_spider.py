import scrapy
from bs4 import BeautifulSoup
from ..items import DangdangItem
"""
    爬取当当网图书畅销榜近七日书籍信息
"""


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allow_dmains = ["http://bang.dangdang.com"]
    start_urls = []
    for page in range(1,26):
        url = ('http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-%s' %(page))
        start_urls.append(url)
        
    def parse(self,response):
        item = DangdangItem()
        data = response.text
        soup = BeautifulSoup(data,'lxml')
        book_list = soup.select('.bang_list.clearfix.bang_list_mode li')
        for book in book_list:
            item['book_name'] = book.select('.name a')[0].get_text()
            item['book_author'] = book.select('.publisher_info a')[0].get_text()
            item['published_time'] = book.select('.publisher_info span')[0].get_text()
            item['publish_house'] = book.select('div.publisher_info a')[-1].get_text()
            item['book_price'] = book.select('.price p .price_n')[0].get_text()
            # 评论数
            item['book_star'] = book.select('.star a')[0].get_text().replace('条评论','')
            yield item






