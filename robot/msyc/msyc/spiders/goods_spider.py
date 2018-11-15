import scrapy
import json
from msyc.items import Catalog
from msyc.items import Goods

class GoodsSpider(scrapy.Spider):
    name = "goods"
    start_urls = ['https://m.msyc.cc/app/product/getLetParent/v3']

    def parse(self, response):
        content = json.loads(response.body)

        catalogs = ({
            'catalog_id': item.get('id'),
            'name': item.get('name'),
            'full_name': item.get('fullName'),
            'state': item.get('state')
        } for data in content.get('data') for item in data.get('data'))

        
        goods_url = 'https://m.msyc.cc/app/product/bycatid/v1?pid=%s&pageNo=1&tmn=1' % '298'
        yield response.follow(goods_url, self.goods_parse)

    def goods_parse(self, response):
        content = json.loads(response.body)
        
        goods = ({
            'goods_id': item.get('id'),
            'name': item.get('name'),
            'quantity': item.get('qty'),
            'props': json.dumps(item.get('goodsProps')),
            'ad_word': item.get('advertise'),
            'brand_id': item.get('brandId'),
            'brand_name': item.get('brandName'),
            'country_id': item.get('countryId'),
            'country_name': item.get('countryName'),
            'fee_price': item.get('freePrice'),
            'image_url': item.get('mainPicUrl'),
            'market_price': item.get('marketPrice'),
            'menu_id': item.get('f_menuId'),
            'catalog_id': item.get('menuId'),
            'catalog_name': item.get('menuName'),
        } for item in content.get('data'))

        for item in goods:
            yield Goods(item)
