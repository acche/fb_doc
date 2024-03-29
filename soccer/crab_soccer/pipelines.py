# -*- coding: utf-8 -*-
import json
from utils.scrapyutils import ItemEncoder

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrabSoccerPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.json', 'wb')  

     
    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False,cls=ItemEncoder) + ",\n"
#         print line
        self.file.write(line)
        return item