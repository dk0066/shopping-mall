# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import requests

class MsycPipeline(object):
    def open_spider(self, spider):
        self.url = 'http://35.220.209.137/parse/classes/'
        self.headers = {'X-Parse-Application-Id': 'shopping-mall-app', 'Content-Type': 'application/json'}

    def process_item(self, item, spider):
        requests.post(self.url + type(item).__name__, data={"country_code": "IT", "country_id": 21, "keyword": "Y", "name": "意大利"}, headers=self.headers)
        spider.log(item)
