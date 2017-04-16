import scrapy
from stocks.models import *
from scrapy.http import Request
import taggit

class ThsCrawler(scrapy.Spider):
    name = "ThsCrawler"
    allowed_domains = ["10jqka.com.cn"]
    start_urls = [
        "http://stockpage.10jqka.com.cn/600340/",
    ]

    def parseStock(self,response):
        #Trim the url to get the stock code
        ticker = response.url[31:-1]
        stock = Stock.objects.get(ticker=ticker)
        tagList = response.xpath('//dl[@class="company_details"]/dd')[1].xpath('@title').extract()[0].split('，')

        #TODO: change set tag operations to incremental update to facilitate reporting
        #self.logger.info(tagList)
        stock.tags.set(*tagList)

    def parse(self,response):
        stocks = Stock.objects.all()

        for stock in stocks:
            url = "http://stockpage.10jqka.com.cn/{}/".format(stock.ticker)
            yield Request(url, callback = self.parseStock)