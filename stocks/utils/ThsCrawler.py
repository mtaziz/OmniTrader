import scrapy
import logging
import sys
from scrapy.crawler import CrawlerProcess


class ThsCrawler(scrapy.Spider):


    name = "ThsCrawler"
    start_urls = [
        "http://stockpage.10jqka.com.cn/600340/",
    ]
    def parse(self,response):
        self.logger.info("world")

        content = response.xpath('//dl[@class="company_details"]/dd')[1].xpath('@title').extract()
        self.logger.info(content)



crawler = ThsCrawler()
crawler.logger.setLevel(logging.INFO)
crawler.logger.info("before")
process = CrawlerProcess()

process.crawl(ThsCrawler)
process.start() # the script will block here until the crawling is finished

crawler.logger.info("after")