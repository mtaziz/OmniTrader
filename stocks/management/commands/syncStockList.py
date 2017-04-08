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
        parser.add_argument('-h', action='store_true', default=False,
                            help='Hard sync and purge the old stock list.')

    def handle(self, *args, **options):
        if options['h'] == True:
            logger.info("Hard sync mode - purge stock list")


        try:
            stock_list = ts.get_today_all()
            if len(stock_list.index) < 3000:
                logger.error("Stock list error - {} in list".format(len(stock_list.index)))
                exit(1)

        except Exception:
            logger.error("Error downloading {} - skipped".format(entry.name))
        with tempinput(io.BytesIO(response.content)) as tempfilename:
            with transaction.atomic():
                extractor = TradeRecordExtractor(tempfilename, date, account, trader)
                extractor.process()
                response.close()
                processed += 1
                tradeRecord = TradeRecord(filename=entry.name, date=date, account=account, trader=trader)
                tradeRecord.save()
                logger.info("{} - success".format(entry.name))
        logger.info("Done - {} files processed, {} skipped.".format(processed, skipped))
        send_mail('OmniTrader - {} trade record processed'.format(processed), '', 'omni.trader.2015@gmail.com',
                  ['andrewmorro@gmail.com'], fail_silently=False)
        return