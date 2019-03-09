# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first() #得到login的token

        #登入資訊
        yield FormRequest('http://quotes.toscrape.com/login',
                          formdata = {'csrf_token':csrf_token,
                                      'username':'footbar',
                                      'password':'footbar'},
                          callback = self.parse_after_login)

    def parse_after_login(self, response):
        """ 如果成功登入，就會打開網頁 """
        open_in_browser(response)
        if response.xpath('//a[text()="Logout"]'):
            self.log('You logged in')