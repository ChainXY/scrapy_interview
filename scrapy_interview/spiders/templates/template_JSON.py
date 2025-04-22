# -*- coding: utf-8 -*-
# AUTHOR: Name
import scrapy
import json
from scrapy.http import Request
from scrapy_interview.items import ChainItem

class TemplateSpider(scrapy.Spider):
    name = "template" #this is the name you use in the scrapy crawl call
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    history = []

    def start_requests(self):
        url = ''
        yield Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        # OPTION 1: JSON in <script>
        script = response.xpath('//*[contains(text(),"var storeLocations")]/text()').extract_first()  ## remove .extract_first() if using .re_first()
        j = script.split('var storeLocations =')[1].split('something')[0] ## script.re_first('locations:\s*(\[.*\]),') #instead of 2 .split()
        stores = json.loads(j)

        # OPTION 2: JSON as the whole response body
        stores = json.loads(response.text)#["features"]
        for store in stores:
            if store['id'] not in self.history:
                self.history.append(store['id'])

                item = ChainItem()

                item['store_name'] = ''
                item['store_type'] = ''
                item['store_uid'] = ''
                item['store_number'] = ''
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
                item['other_fields'] = '' #json of other information that can be captured by location
                item['coming_soon'] = '' #boolean
                yield item
