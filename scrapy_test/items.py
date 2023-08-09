import scrapy

class WebsiteItem(scrapy.Item):
    url = scrapy.Field()
    phone_numbers = scrapy.Field()
    logo_urls = scrapy.Field()
