from django.core.management.base import BaseCommand, CommandError
from stocks.models import Stock, DayData
from django.db import transaction

import csv
import codecs
import urllib.request
import multiprocessing


# reference:http://stackoverflow.com/questions/18897029/read-csv-file-from-url-into-python-3-x-csv-error-iterator-should-return-str
# add atomic annotation to enable batch commit and improve performance
@transaction.atomic
def importHistoricalDataForStock(ticker=str):
    stock = Stock.objects.get(ticker=ticker)
    # add corresponding suffix according to the market(ss for Shanghai while sz for Shenzhen
    url = 'http://table.finance.yahoo.com/table.csv?s='+ticker+(ticker.startswith('60') and '.ss' or '.sz')
    print('Import day quote data for {}({}) from source: {}'.format(stock.name,stock.ticker,url))
    response = urllib.request.urlopen(url)
    reader = csv.reader(codecs.iterdecode(response, 'utf-8'))

    #skip first header row
    next(reader)

    # save day quote data to db
    for row in reader:
        obj = DayData(stock=stock,date=row[0],open=row[1],high=row[2],low=row[3],close=row[4],volume=row[5],adj_close=row[6])
        obj.save()

class Command(BaseCommand):
    help = 'Load historical data for stocks'

    def add_arguments(self, parser):
        parser.add_argument('--ticker', nargs='?', type=str, help='tickers of the stocks to be imported')
        parser.add_argument('--all', action='store_true', default=False, help='import all stocks')

    def handle(self, *args, **options):
        if options['all']==True:
            pool = multiprocessing.Pool(50)
            pool.map(importHistoricalDataForStock, Stock.objects.values_list('ticker',flat=True))
        elif options['ticker']!=None:
            for ticker in options['ticker']:
                try:
                    importHistoricalDataForStock(ticker)
                except Stock.DoesNotExist:
                    print('Stock "%s" does not exist' % ticker)
                    next
                self.stdout.write('Successfully imported day data for stock "%s"' % ticker)
        else:
            print('Error: Please specify the tickers or use --all option')


    