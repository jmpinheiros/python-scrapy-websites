#!/usr/bin/env python3
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

        # Extract phone numbers and perform light cleaning
        # Brasil e USA
        phone_numbers = re.findall(
            r'\b(?:\+\d{2}\s?)?'  # Country code
            r'(?:\(\d{3}\)\s?\d{3}[-\s]?\d{4}'  # (xxx) xxx-xxxx
            r'|'  # OR
            r'\d{3}[-\s]?\d{3}[-\s]?\d{4}'  # xxx-xxx-xxxx
            r'|'  # OR
            r'\d{3}\s\d{3}[-\s]?\d{4}'  # xxx xxx xxxx
            r'|'  # OR
            r'\d{4}[-\s]?\d{4}'  # xxxx-xxxx
            r'|'  # OR
            r'0800\s\d{3}[-\s]?\d{4}'  # 0800 xxx-xxxx
            r'|'  # OR
            r'4004\s\d{4}'  # 4004 xxxx
            r'|'  # OR
            r'1-\d{3}-\d{3}-\d{4}'  # 1-xxx-xxx-xxxx
            r'|'  # OR
            r'\+\d\s?\d{3}[-\s]?\d{3}[-\s]?\d{4}'  # +x xxx-xxx-xxxx
            r')\b', text
        )

        cleaned_phone_numbers = [self.clean_phone_number(
            number) for number in phone_numbers]
        unique_phone_numbers = list(set(cleaned_phone_numbers))

        # Extract logo image URLs
        logo_urls = response.css('img[src*=logo]::attr(src)').getall()

        # Output the results
        item = WebsiteItem()
        item['url'] = response.url
        item['phone_numbers'] = unique_phone_numbers
        item['logo_urls'] = [urljoin(response.url, url) for url in logo_urls]
        yield item

    def clean_phone_number(self, number):
        cleaned_number = re.sub(r'[^\d+() ]', ' ', number)
        # Replace multiple spaces with a single space
        cleaned_number = re.sub(r'\s+', ' ', cleaned_number)
        cleaned_number = cleaned_number.strip()

        # Add parentheses if the number is in "xxx xxx xxxx" or "1 xxx xxx xxxx" format
        if re.match(r'^\d{3} \d{3} \d{4}$', cleaned_number):
            cleaned_number = '(' + \
                cleaned_number[:3] + ') ' + cleaned_number[4:]

        elif re.match(r'^1 \d{3} \d{3} \d{4}$', cleaned_number):
            cleaned_number = '1 (' + \
                cleaned_number[2:5] + ') ' + cleaned_number[6:]

        return cleaned_number