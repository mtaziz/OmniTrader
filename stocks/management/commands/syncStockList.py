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

        added = 0
        changed = 0
        email_body = ''
        stock_list = ts.get_today_all()
        count = len(stock_list.index)
        logger.info("Tushare : {} stocks in list".format(count))
        if count < 3000:
            exit(1)
        stock_store = Stock.objects.all()
        for index, row in stock_list.iterrows():
            try:
                stock = stock_store.get(ticker = row['code'])
                if stock.name != row['name']:
                    with transaction.atomic():
                        old_name = stock.name
                        stock.name = row['name']
                        stock.save()
                        changed += 1
                        msg = "{} has changed name from {} to {}".format(row['code'], old_name, row['name'])
                        email_body += msg + '\n'
                        logger.info(msg)
            except ObjectDoesNotExist as e:
                with transaction.atomic():
                    stock = Stock(ticker=row['code'], name=row['name'])
                    stock.save()
                    added += 1
                    msg = "TODO: add stock {} {}".format(row['code'], row['name'])
                    email_body += msg + '\n'
                    logger.info(msg)
        email_title = "OmniTrader Sync Stock List - {} stocks added, {} changed.".format(added, changed)
        logger.info(email_title)
        send_mail(email_title, email_body, 'omni.trader.2015@gmail.com',
         ['andrewmorro@gmail.com'], fail_silently=False)
        return

