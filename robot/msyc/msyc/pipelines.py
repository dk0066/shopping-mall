# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import requests
import urllib

class MsycPipeline(object):
    def open_spider(self, spider):
        self.url = 'http://35.220.209.137/parse/classes/'
        self.headers = {'X-Parse-Application-Id': 'shopping-mall-app', 'Content-Type': 'application/json'}

    def process_item(self, item, spider):
        data = item.__dict__['_values']
        response = requests.post(self.url + type(item).__name__, data=json.dumps(data), headers=self.headers)

    def has_country(self, item):
        params = urllib.parse.quote(json.dumps({"where": {"country_id": 47}}))
        r = requests.get(self.url + type(item).__name__ + "?" + params, headers=self.headers)
        result = json.loads(r.test)

        print(result)
        
