# -*- coding: utf-8 -*-
import scrapy
import re
import html2text
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
        # Convert HTML to text
        h = html2text.HTML2Text()
        h.ignore_links = True
        text = h.handle(response.text)

        # Extract phone numbers - Brazil, USA, 
        phone_numbers = re.findall(
            r'\b(?:\+\d{2}\s?)?(?:(?:\d{2}\s\d{2}\s\d{9})|(?:\d{4}\s\d{3}\s\d{4})|(?:\d{4}\s\d{4})'
            r'|(?:0800\s\d{3}\s\d{4})|(?:\(?\d{3}\)?\s?\d{4}\s?\d{4})|(?:\(\d{3}\)\s?\d{3}-\d{4})'
            r'|(?:\d{3}-\d{4})|(?:\(\d{3}\)\s\d{3}-\d{4})|(?:1-\d{3}-\d{3}-\d{4})'
            r'|(?:\(?\d{3}\)?\s?\d{3}-\d{4})|(?:\(?\d{3}\)?\s?\d{3}-?\d{4}\)?)'
            r'|(?:\(?\d{3}\)?\s?\d{4}-?\d{4}\)?))\b',
            text
        )

        # Use set to avoid duplicate phone numbers
        unique_phone_numbers = set(phone_numbers)

        # Extract logo image URLs
        logo_urls = response.css('img[src*=logo]::attr(src)').getall()

        # Output the results
        item = WebsiteItem()
        item['url'] = response.url
        item['phone_numbers'] = list(unique_phone_numbers)
        item['logo_urls'] = [urljoin(response.url, url) for url in logo_urls]
        yield item