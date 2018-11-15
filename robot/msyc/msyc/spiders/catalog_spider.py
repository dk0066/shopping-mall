import scrapy
import json
from msyc.items import Catalog

class CatalogSpider(scrapy.Spider):
    name = "catalog"
    start_urls = ['https://m.msyc.cc/app/product/getLetParent/v3']

    def parse(self, response):
        content = json.loads(response.body)

        catalogs = ({
            'id': item.get('id'),
            'name': item.get('name'),
            'full_name': item.get('fullName'),
            'state': item.get('state')
        } for data in content.get('data') for item in data.get('data'))

        for item in catalogs:
            yield Catalog(item)
