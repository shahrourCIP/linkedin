# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class QuoteItemElse(scrapy.Item):
    text = scrapy.Field()
    
class opExper(scrapy.Item):
    for oneof in scrapy.Selector:
        text = scrapy.Field()
        
