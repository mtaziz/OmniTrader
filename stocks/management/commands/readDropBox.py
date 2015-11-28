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

logger = logging.getLogger('stocks.management.readDropbox')

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
    def handle(self, *args, **options):
        logger.info("Reading Dropbox...")
        dbx = dropbox.Dropbox('DO8936TNbkgAAAAAAAAAg4zB4LdJK2SBNBPdjaTWM5mpzjU8dFmp1MV5DNiEXDzk')
        skipped = 0
        processed = 0
        for entry in dbx.files_list_folder('/业绩单',recursive=True).entries:
            if not isinstance(entry, FileMetadata):
                continue
            logger.info("Processing: {}".format(entry.path_lower))
            res = re.search("(.+)(\d{4}-\d{2}-\d{2})[\s+]?(.+).xls",entry.name)
            if res:
                try:
                    trader = Trader.objects.get(name=res.group(3))
                    date = res.group(2)
                    account = Account.objects.get(name=res.group(1))
                except ObjectDoesNotExist:
                    logger.error("Either the trader or account doesn't exist.")
                    continue
            else:
                logger.error("Unable to extract information from {}".format(entry.name))
                continue


            if TradeRecord.objects.filter(filename=entry.name,trader = trader,account = account, date = date).count()>0 :
                logger.info("File {} has been loaded - skipped.".format(entry.name))
                skipped += 1
                continue
            

            try:
                metadata,response = dbx.files_download(entry.path_lower)
            except Exception:
                logger.error("Error downloading {} - skipped".format(entry.name))
                continue
            with tempinput(io.BytesIO(response.content)) as tempfilename:
                with transaction.atomic():
                    extractor = TradeRecordExtractor(tempfilename, date, account, trader)
                    extractor.process()
                    response.close()
                    processed += 1
                    tradeRecord = TradeRecord(filename = entry.name, date = date, account = account, trader = trader)
                    tradeRecord.save()
                    logger.info("{} - success".format(entry.name))
        logger.info("Done - {} files processed, {} skipped.".format(processed,skipped))
        return