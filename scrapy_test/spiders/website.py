import scrapy


# class WebsiteSpider(scrapy.Spider):
#     name = "website"
#     allowed_domains = ["example.com"]
#     start_urls = ["https://example.com"]

#     def parse(self, response):
#         pass



import re
from urllib.parse import urljoin
from scrapy_test.items import WebsiteItem

class WebsiteSpider(scrapy.Spider):
    name = 'website'

    def __init__(self, *args, **kwargs):
        super(WebsiteSpider, self).__init__(*args, **kwargs)
        self.urls = kwargs.get('urls', '').splitlines()

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract phone numbers
        phone_numbers = re.findall(r'\+?[()\d\s-]+', response.text)
        cleaned_phone_numbers = [re.sub(r'[^\d+()]', ' ', number).strip() for number in phone_numbers]

        # Extract logo image URLs
        logo_urls = response.css('img[src*=logo]::attr(src)').getall()

        # Output the results
        item = WebsiteItem()
        item['url'] = response.url
        item['phone_numbers'] = cleaned_phone_numbers
        item['logo_urls'] = [urljoin(response.url, url) for url in logo_urls]
        yield item

