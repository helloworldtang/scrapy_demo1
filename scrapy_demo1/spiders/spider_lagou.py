# -*- coding: utf-8 -*-
import scrapy


class SpiderLagouSpider(scrapy.Spider):
    name = 'spider_lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']

    def parse(self, response):
        pass
