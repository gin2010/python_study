# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KylinosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    position = scrapy.Field()
    num = scrapy.Field()
    location = scrapy.Field()
    duty = scrapy.Field()
    request = scrapy.Field()
    note = scrapy.Field()
