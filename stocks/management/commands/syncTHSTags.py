from django.core.management.base import BaseCommand, CommandError
from stocks.utils.TradeRecordExtractor import TradeRecordExtractor
import dropbox
from time import sleep
import urllib3
from stocks.models import *
import re

import os
import tempfile
import shutil
import socket
from contextlib import contextmanager
from dropbox.files import DownloadError, FileMetadata
import io
import logging
from django.db import transaction
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

import tushare as ts

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import scrapy



logger = logging.getLogger('stocks.management.syncTHSTags')


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-r', action='store_true', default=False,
                            help='Hard sync and purge the old stock list.')
    @classmethod
    def parse(self, response):

        print('world')
        print(response.body)
        return ''

    def handle(self, *args, **options):
        if options['r'] == True:
            logger.info("Hard sync mode - purge stock list")

        stock_store = Stock.objects.all()

        print('hello')
        yield scrapy.Request(url='http://stockpage.10jqka.com.cn/600340/', callback=Command.parse)

        #print(response.xpath('//dl[@class="company_details"]/dd'))
        #result = response.xpath('//dl[@class="company_details"]/dd')[1].xpath('@title').extract()
        #print(result)
        return

