# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from spidertest.items import SpidertestItem


class NovelSpider(scrapy.Spider):
    name = "novel"
    start_urls = [
        'https://www.readnovel.com/all?pageSize=10&gender=2&catId=-1&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum=1']
    pre_url = 'https://www.readnovel.com/all?pageSize=10&gender=2&catId=-1&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum='

    def parse(self, response):
        books = response.xpath("//div[@class='right-book-list']/ul/li")
        item = SpidertestItem()
        for book in books:
            item["book_image"] = book.xpath("./div[@class='book-img']/a/img/@src").extract()[0]
            book_info = book.xpath("./div[@class='book-info']")
            item["book_id"] = book_info.xpath("./h3/a/@href").extract()[0].split("/")[2]
            item["book_title"] = book_info.xpath("./h3/a/text()").extract()[0]
            item["book_author"] = book_info.xpath("./h4/a/text()").extract()[0]
            item["book_category"] = book_info.xpath("./p[@class='tag']/span[@class='org']/text()").extract()[0]
            item["book_serialstatus"] = book_info.xpath("./p[@class='tag']/span[@class='red']/text()").extract()[0]
            item["book_serialnumber"] = book_info.xpath("./p[@class='tag']/span[@class='blue']/text()").extract()[0]
            item["book_desc"] = book_info.xpath("./p[@class='intro']/text()").extract()
            yield item

        current_page = int(response.xpath("//div[@id='page-container']/@data-page").extract()[0])
        print(current_page)
        if current_page >=100:
            return
        yield scrapy.Request(self.pre_url + str(current_page + 1), callback=self.parse)
