import scrapy
from stocks.models import *
from scrapy.http import Request
import logging
import taggit

class ThsCrawler(scrapy.Spider):
    name = "ThsCrawler"
    allowed_domains = ["10jqka.com.cn"]
    start_urls = [
        "http://stockpage.10jqka.com.cn/600340/",
    ]
    def ThsCrawler(self):
        self.logger.setLevel(logging.INFO)

    def parseStock(self,response):
        #Trim the url to get the stock code
        ticker = response.url[31:-1]
        stock = Stock.objects.get(ticker=ticker)
        content = response.xpath('//dl[@class="company_details"]/dd')
        location = content[0].xpath('text()').extract()[0]
        #self.logger.info(location)
        tagList = response.xpath('//dl[@class="company_details"]/dd')[1].xpath('@title').extract()[0].split('，')

        #TODO: change set tag operations to incremental update to facilitate reporting
        #self.logger.info(tagList)
        stock.tags.set(location, *tagList)

    def parse(self,response):
        stocks = Stock.objects.all()

        for stock in stocks:
            url = "http://stockpage.10jqka.com.cn/{}/".format(stock.ticker)
            yield Request(url, callback = self.parseStock)