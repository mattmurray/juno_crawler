# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JunoCrawlerItem(scrapy.Item):
    artist = scrapy.Field()
    title = scrapy.Field()
    label = scrapy.Field()
    tracks = scrapy.Field()
    catalog_number = scrapy.Field()
    release_date = scrapy.Field()
    genre = scrapy.Field()
