# -*- coding: utf-8 -*-
import scrapy


class MybotSpider(scrapy.Spider):
    name = 'mybot'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
        	text = quote.xpath('.//*[@class ="text"]/text()').extract_first()
        	author = quote.xpath('.//*[@class ="author"]/text()').extract_first()
        	tags = quote.xpath('.//*[@class ="keywords"]/@content').extract_first()

        	yield  {'Text' : text,
                     'Author' :author,
        	         'Tags':tags}

       	# 翻頁
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url  = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)