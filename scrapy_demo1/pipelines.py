# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyDemo1Pipeline(object):
    def __init__(self) -> None:
        super().__init__()

    def process_item(self, item, spider):
        print("item:", item["urlTitle"])
        return item
