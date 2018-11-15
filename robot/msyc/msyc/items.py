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

class Brand(scrapy.Item):
    brand_id = scrapy.Field()
    name = scrapy.Field()
    logo = scrapy.Field()
    keyword = scrapy.Field()

class Catalog(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    full_name = scrapy.Field()
    state = scrapy.Field()

class Goods(scrapy.Item):
    goods_id = scrapy.Field()
    name = scrapy.Field()
    quantity = scrapy.Field()
    props = scrapy.Field()
    image_url = scrapy.Field()
    ad_word = scrapy.Field()
    brand_id = scrapy.Field()
    brand_name = scrapy.Field()
    country_id = scrapy.Field()
    country_name = scrapy.Field()
    fee_price = scrapy.Field()
    market_price = scrapy.Field()
    menu_id = scrapy.Field()
    catalog_id = scrapy.Field()
    catalog_name = scrapy.Field()