import scrapy
from stocks.models import *
from scrapy.http import Request

class HolderCrawler(scrapy.Spider):
    name = "HolderCrawler"
    allowed_domains = ["10jqka.com.cn"]
    start_urls = [
        "http://stockpage.10jqka.com.cn/600340/",
    ]

    def parseHolder(self,response):
        #Trim the url to get the stock code
        ticker = response.url[31:37]
        stock = Stock.objects.get(ticker=ticker)
        content = response.xpath('//dl[@class="company_details"]/dd')
        location = content[0].xpath('text()').extract()[0]
        #self.logger.info(location)
        tagList = response.xpath('//dl[@class="company_details"]/dd')[1].xpath('@title').extract()[0].split('，')



    def parse(self,response):

        stocks = Stock.objects.all()

        for stock in stocks:
            url = "http://stockpage.10jqka.com.cn/{}/holder".format(stock.ticker)
            yield Request(url, callback = self.parseHolder)