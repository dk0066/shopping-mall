import scrapy
import json
from msyc.items import Country

class CountrySpider(scrapy.Spider):
    name = "country"
    start_urls = ['https://m.msyc.cc/product/countrys']

    def parse(self, response):
        countries = [{
            'country_id': element['countryId'],
            'country_code': element['code'],
            'name': element['name'],
            'keyword': element['word']
        } for element in json.loads(response.body)]

        for item in countries:
            yield Country(item)
