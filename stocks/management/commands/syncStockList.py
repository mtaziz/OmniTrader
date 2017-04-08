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
from contextlib import contextmanager
from dropbox.files import DownloadError, FileMetadata
import io
import logging
from django.db import transaction
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

import tushare as ts

logger = logging.getLogger('stocks.management.syncStockList')


@contextmanager
def tempinput(file_):
    temp = tempfile.NamedTemporaryFile(delete=False)

    shutil.copyfileobj(file_, temp)
    temp.close()
    logger.debug('temp file created')
    yield temp.name
    os.unlink(temp.name)
    logger.debug('temp file deleted')


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-r', action='store_true', default=False,
                            help='Hard sync and purge the old stock list.')

    def handle(self, *args, **options):
        if options['r'] == True:
            logger.info("Hard sync mode - purge stock list")


        stock_list = ts.get_today_all()
        if len(stock_list.index) < 3000:
            logger.error("Stock list error - {} in list".format(len(stock_list.index)))
            exit(1)
        for index, row in stock_list.iterrows():
            print(row['code'])
            try:
                stock = Stock.objects.get(ticker = row['code'])
                print(stock.name)
            except ObjectDoesNotExist as e:
                print("TODO: add stock")
            #logger.info("Done - {} files processed, {} skipped.".format(processed, skipped))
        #send_mail('OmniTrader - {} trade record processed'.format(processed), '', 'omni.trader.2015@gmail.com',
        # ['andrewmorro@gmail.com'], fail_silently=False)
        return

