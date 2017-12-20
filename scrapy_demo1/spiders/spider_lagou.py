# -*- coding: utf-8 -*-
import scrapy

from scrapy_demo1.items import ScrapyDemo1Item


class SpiderLagouSpider(scrapy.Spider):
    name = 'spider_lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']

    def parse(self, response):
        lagouItem = ScrapyDemo1Item()
        lagouItem["urlTitle"] = response.xpath("/html/head/title/text()")
        print("lagouItem:", lagouItem)
        print("lagouItem:", lagouItem["urlTitle"])
