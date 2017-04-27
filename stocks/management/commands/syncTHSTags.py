from django.core.management.base import BaseCommand, CommandError
import logging
from scrapy.crawler import CrawlerProcess
from stocks.utils.ThsCrawler import ThsCrawler

from django.core.mail import send_mail

logger = logging.getLogger('stocks.management.syncTHSTags')


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-r', action='store_true', default=False,
                            help='Hard sync and purge the old stock list.')


    def handle(self, *args, **options):
        process = CrawlerProcess({
            'LOG_LEVEL': 'INFO',
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(ThsCrawler)
        process.start()  # the script will block here until the crawling is finished
        email_title = 'OmniTrader THS Tag Sync completed.'
        send_mail(email_title, '', 'omni.trader.2015@gmail.com',
                  ['andrewmorro@gmail.com'], fail_silently=False)



