# -*- coding: utf-8 -*-
# AUTHOR: Unknown
# FIX: Rewritten - it is super banned, use US-New Jersey-1 VPN from ExpressVPN or try different ones. Couldn't figure it out the JSON or Selenium - captcha, Jun 9 2020, FL
import scrapy
import json
from scrapy_interview.items import ChainItem
from scrapy import Request
import scrapy_interview.utils as utils



class LondondrugsSpider(scrapy.Spider):
    name = "londondrugs"
    #valid scrape_type values: html - single-page, html - multi-page, json - single-page, kml, selenium, other
    scrape_type = "html - single-page" #GENERATED AUTOMATICALLY - VERIFY!
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    # handle_httpstatus_list = [302]

    def start_requests(self):
        url = 'https://www.londondrugs.com/all-store-locations/?context=storeLocator'
        yield Request(url = url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        stores = response.xpath('//*[@class="all-stores"]//li')
        for store in stores:
            item = ChainItem()
            item['store_name'] = utils.stripList(store.xpath('.//h3//text()').extract())[0]
            item['store_number'] = ''
            item['store_type'] = ''
            item['address'] = store.xpath('.//*[@itemprop="streetAddress"]/text()').extract_first()
            item['address2'] = ''
            item['city'] = store.xpath('.//*[@itemprop="addressLocality"]/text()').extract_first()
            item['state'] = store.xpath('.//*[@itemprop="addressRegion"]/text()').extract_first()
            # if item['state'] == 'Alberta':
            #     continue
            item['zip_code'] = store.xpath('.//*[@itemprop="postalCode"]/text()').extract_first()
            item['country'] = 'CA'
            item['phone_number'] = store.xpath('.//*[@itemprop="telephone"]/text()').extract_first()
            item['latitude'] = ''
            item['longitude'] = ''
            item['store_hours'] = ''
            item['other_fields'] = ''
            item['coming_soon'] = ''
            yield item

    # GOOD CODE BUT BANNED
    # def start_requests(self):
    #     url = 'https://www.londondrugs.com/on/demandware.store/Sites-LondonDrugs-Site/default/MktStoreList-All'
    #     yield scrapy.Request(url = url, callback = self.parse)
    #
    # def parse(self, response):
    #     stores = json.loads(response.text)
    #
    #     for store in stores:
    #         item = ChainItem()
    #
    #         item['store_name'] = store['name']
    #         item['store_number'] = store['id']
    #         item['address'] = store['address1']
    #         item['address2'] = store['address2']
    #         item['city'] = store['city']
    #         item['state'] = store['stateCode']
    #         item['zip_code'] = store['postalCode']
    #         item['country'] = store['countryCode']
    #         item['latitude'] = store['latitude']
    #         item['longitude'] = store['longitude']
    #         item['phone_number'] = store['phone']
    #         item['attributes']= {}
    #
    #         store_hours = ''
    #         for hrs_type in store['storeHours']:
    #             if hrs_type['type'] == "Store Hours":
    #                 for day in hrs_type['storeHours']:
    #                     if day['day'] != 'Holidays':
    #                         store_hours += day['day'] +": "+ day['hours'][0] + "-" + day['hours'][1] + ", "
    #                 item['store_hours'] = store_hours
    #
    #             if hrs_type['type'] == "Pharmacy Hours":
    #                 for day in hrs_type['storeHours']:
    #                     if day['day'] != 'Holidays':
    #                         store_hours += day['day'] +": "+ day['hours'][0] + "-" + day['hours'][1] + ", "
    #                 item['attributes']['RXHOURS'] = store_hours
    #
    #         if 'PICKUP' in item['store_name'].upper():
    #             item['store_type'] = "Pickup Location"
    #             item['store_name'] = item['store_name'].replace('London Drugs Pickup Location - ', '')
    #             # item['distributor_name'] = item['store_name'].replace('London Drugs Pickup Location - ','')
    #
    #         elif 'LD EXPRESS' in item['store_name'].upper():
    #             item['store_type'] = "LDExpress Store"
    #         else:
    #             item['store_type'] = "London Drugs Store"
    #             item['store_name'] = "London Drugs - " + item['store_name']
    #
    #         item['other_fields'] = ""
    #         item['coming_soon'] = "0"
    #         yield item
