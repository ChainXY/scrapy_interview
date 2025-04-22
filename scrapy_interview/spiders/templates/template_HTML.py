# -*- coding: utf-8 -*-
# AUTHOR: Name

import scrapy
from scrapy.http import Request
from scrapy_interview.items import ChainItem

class TemplateSpider(scrapy.Spider):
    name = "template" #this is the name you use in the scrapy crawl call
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

    def start_requests(self):
        url = ''
        yield Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        stores = response.xpath('')
        for store in stores:
            item = ChainItem()
            item['store_name'] = store.xpath('.').extract_first()
            item['store_number'] = ''
            item['store_type'] = ''
            item['address'] = '' 
            item['address2'] = ''
            item['city'] = ''
            item['state'] = ''
            item['zip_code'] = ''
            item['country'] = ''
            item['phone_number'] = ''
            item['latitude'] = ''
            item['longitude'] = ''
            item['store_hours'] = '' #comma-separated list of open hours by day
            item['other_fields'] = '' #other information that can be captured by location
            item['coming_soon'] = '' #boolean
            yield item
