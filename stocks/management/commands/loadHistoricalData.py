from django.core.management.base import BaseCommand, CommandError
from stocks.models import Stock, DayData
from django.db import transaction
from django.db.models import Max,Count
from concurrent.futures import ThreadPoolExecutor
from socket import timeout

import datetime
import time
import csv
import codecs
import urllib.request

import threading
from urllib.error import HTTPError, URLError


# reference:http://stackoverflow.com/questions/18897029/read-csv-file-from-url-into-python-3-x-csv-error-iterator-should-return-str
# this method is called by the pool worker. That's why it sits outside the Command class - to be pickled.
# add atomic annotation to enable batch commit and improve performance
@transaction.atomic
def importHistoricalDataForStock(ticker=str):
    
    #if  not ticker.startswith('603'):
    #    return

    stock = Stock.objects.get(ticker=ticker)
    # Skip stocks that already loaded

    # Data source from yahoo will append record for each day even if the stock is suspended. 
    # Thus, if there's any day record of the stock, there're all of them from the beginning to the latest(atomic transaction)
    if stock.dayHist.count() > 0 :
        print('{} - skip {}({}) : already loaded'.format(threading.get_ident(),stock.name,stock.ticker))
    else:
        # add corresponding suffix according to the market(ss for Shanghai while sz for Shenzhen
        url = 'http://table.finance.yahoo.com/table.csv?s='+ticker+(ticker.startswith('60') and '.ss' or '.sz')
        print('{} - import day quote data for {}({}) from source: {}'.format(threading.get_ident(),stock.name,stock.ticker,url))
        try:

            response = urllib.request.urlopen(url,timeout=300)
            reader = csv.reader(codecs.iterdecode(response, 'utf-8'))

            #skip first header row
            next(reader)
            # save day quote data to db
            for row in reader:
                obj = DayData(stock=stock,date=row[0],open=row[1],high=row[2],low=row[3],close=row[4],volume=row[5],adj_close=row[6])
                obj.save()
        except(HTTPError, URLError) as error:
            print('{} - "HTTP or URL Error! - {}({})'.format(threading.get_ident(),stock.name,stock.ticker))
            transaction.rollback()
            return
        except timeout:
            print('{} - "Timeout - {}({})'.format(threading.get_ident(),stock.name,stock.ticker))
            transaction.rollback()
            return
        else:
            time.sleep(1)

class Command(BaseCommand):
    help = 'Load historical data for stocks'

    def add_arguments(self, parser):
        parser.add_argument('--ticker', nargs='?', type=str, help='tickers of the stocks to be imported')
        parser.add_argument('--all', action='store_true', default=False, help='import all stocks')

    def handle(self, *args, **options):

        if options['all']==True:
            with ThreadPoolExecutor(max_workers=50) as executor:
                tickers = Stock.objects.values_list('ticker',flat=True);
                executor.map(importHistoricalDataForStock, tickers)
                executor.shutdown(wait=True)
        elif options['ticker']!=None:
            for ticker in options['ticker'].split(','):
                try:
                    importHistoricalDataForStock(ticker)
                except Stock.DoesNotExist:
                    print('Stock "%s" does not exist' % ticker)
                    next
                self.stdout.write('Successfully imported day data for stock "%s"' % ticker)
        else:
            print('Error: Please specify the tickers or use --all option')


    