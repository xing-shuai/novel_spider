# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class SpidertestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    book_title=Field()#小说名字

    book_author=Field()#作者

    book_image=Field()#链接

    book_serialstatus=Field()#连载状态

    book_serialnumber=Field()#字数

    book_category=Field()#类别

    book_id=Field()#小说编号

    book_desc=Field()#描述


