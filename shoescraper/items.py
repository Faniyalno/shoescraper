# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FtwearItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    size_lists = scrapy.Field()
    vendor = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()