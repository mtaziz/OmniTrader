import scrapy
from stocks.models import *
from scrapy.http import Request
import logging
import taggit
from django.core.mail import send_mail

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
        content = response.xpath('//dl[@class="company_details"]/dd')
        location = content[0].xpath('text()').extract()[0]
        #self.logger.info(location)
        tagList = response.xpath('//dl[@class="company_details"]/dd')[1].xpath('@title').extract()[0].split('，')

        newtags = [item for sublist in [tagList, [location]] for item in sublist]

        oldtags = stock.tags.names()

        tempDict = {}

        email_body = ''

        for tag in newtags:
            if tag in oldtags:
                #self.logger.info('{} existed - Skip'.format(tag))
                tempDict[tag] = True
            else:
                self.logger.info('Add {}'.format(tag))
                tempDict[tag] = True
                stock.tags.add(tag)
        # Disable removal - Avoid removing manual tags
        '''
        for tag in oldtags:
            if tag not in tempDict:
                self.logger.info('Remove {}'.format(tag))
                stock.tags.remove(tag)
        '''
        #self.logger.info(tagList)
        #stock.tags.set(location, *tagList)
        #send_mail('Tag sync completed', email_body, 'omni.trader.2015@gmail.com',
        #                  ['andrewmorro@gmail.com'], fail_silently=False)


    def parse(self,response):
        stocks = Stock.objects.all()

        for stock in stocks:
            url = "http://stockpage.10jqka.com.cn/{}/".format(stock.ticker)
            yield Request(url, callback = self.parseStock)