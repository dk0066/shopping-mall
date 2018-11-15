import scrapy
import json
from msyc.items import Brand

class BrandSpider(scrapy.Spider):
    name = "brand"
    start_urls = ['https://m.msyc.cc/product/brandword']

    def parse(self, response):
        data = json.loads(response.body)

        print(data)

        brands = ({
            'brand_id': item.get('brand_id'),
            'name': item.get('brand_name'),
            'logo': item.get('brand_url', ''),
            'keyword': item.get('word', '')
        } for key, value in data.items() for item in value)

        for item in brands:
            yield Brand(item)
