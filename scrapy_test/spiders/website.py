import scrapy


class WebsiteSpider(scrapy.Spider):
    name = "website"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
