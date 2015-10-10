from django.core.management.base import BaseCommand, CommandError

from django.db import transaction

@transaction.atomic
def extractTrade(path=str):
    print('')
    
class Command(BaseCommand):
    help = 'Extract trades from pnl sheets'
    print('test')
    worker_num = 10

    def add_arguments(self, parser):
        parser.add_argument('--ticker', nargs='?', type=str, help='tickers of the stocks to be imported')
        parser.add_argument('--all', action='store_true', default=False, help='import all stocks')

    def handle(self, *args, **options):
        print(help)
        f = open(r'F:\BaiduSync\trade\ҵ����\������2015-09-10����.xls','r')




        return
        if options['all']==True:
            with ThreadPoolExecutor(max_workers=self.worker_num) as executor:
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
                #self.stdout.write('Successfully imported day data for stock "%s"' % ticker)
        else:
            print('Error: Please specify the tickers or use --all option')


    