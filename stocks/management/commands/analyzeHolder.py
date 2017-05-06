from django.core.management.base import BaseCommand, CommandError
import logging
from scrapy.crawler import CrawlerProcess
from stocks.utils.HolderCrawler import HolderCrawler
import datetime

logger = logging.getLogger('stocks.management.syncTHSTags')


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-d')


    def handle(self, *args, **options):
        filename = datetime.datetime.now().strftime('%Y%m%d')
        if options['d'] is not None:
            filename = options['d']
        process = CrawlerProcess({
            'LOG_LEVEL': 'INFO',
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'ITEM_PIPELINES': {
                'stocks.utils.HolderCrawler.FlowValueItemPipeline': 400
            }
        })
        process.crawl(HolderCrawler, filepath=r"C:\Users\Andrew\Desktop\{}.xlsx".format(filename))
        process.start()  # the script will block here until the crawling is finished

        print('Finished - Crawl flow value holder.')

