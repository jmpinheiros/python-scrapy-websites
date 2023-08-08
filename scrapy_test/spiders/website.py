# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urljoin
from scrapy_test.items import WebsiteItem



# import scrapy
# import re
# from urllib.parse import urljoin
# from scrapy_test.items import WebsiteItem

# class WebsiteSpider(scrapy.Spider):
#     name = 'website'

#     def __init__(self, *args, **kwargs):
#         super(WebsiteSpider, self).__init__(*args, **kwargs)
#         self.urls_file = kwargs.get('urls_file')

#     def start_requests(self):
#         with open(self.urls_file, 'r') as f:
#             urls = f.read().splitlines()

#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         # Extract phone numbers
#         phone_numbers = re.findall(r'\+?[()\d\s-]+', response.text)
#         cleaned_phone_numbers = [re.sub(r'[^\d+()]', ' ', number).strip() for number in phone_numbers]

#         # Extract logo image URLs
#         logo_urls = response.css('img[src*=logo]::attr(src)').getall()

#         # Output the results
#         item = WebsiteItem()
#         item['url'] = response.url
#         item['phone_numbers'] = cleaned_phone_numbers
#         item['logo_urls'] = [urljoin(response.url, url) for url in logo_urls]
#         yield item



import scrapy
import re
from urllib.parse import urljoin
from scrapy_test.items import WebsiteItem

class WebsiteSpider(scrapy.Spider):
    name = 'website'

    def __init__(self, *args, **kwargs):
        super(WebsiteSpider, self).__init__(*args, **kwargs)
        self.urls_file = kwargs.get('urls_file')

    def start_requests(self):
        with open(self.urls_file, 'r') as f:
            urls = f.read().splitlines()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract phone numbers
        phone_numbers = re.findall(r'\b\d{2}\s\d{2}\s\d{9}\b', response.text)

        # Extract logo image URLs
        logo_urls = response.css('img[src*=logo]::attr(src)').getall()

        # Output the results
        item = WebsiteItem()
        item['url'] = response.url
        item['phone_numbers'] = phone_numbers
        item['logo_urls'] = [urljoin(response.url, url) for url in logo_urls]
        yield item