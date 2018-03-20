# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class SpidertestPipeline(object):
    def __init__(self):
        # 打开文件
        self.file = open('data.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n\n"
        # 写入文件
        self.file.write(line)

        return item

    def close_spider(self, spider):
        self.file.close()