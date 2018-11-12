# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Country(scrapy.Item):
    # define the fields for your item here like:
    country_id = scrapy.Field()
    country_code = scrapy.Field()
    name = scrapy.Field()
    keyword = scrapy.Field()
    pass
