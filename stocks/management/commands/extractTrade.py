from django.core.management.base import BaseCommand, CommandError

from django.db import transaction
from stocks.models import Trade,Trader,Account,Stock
import xlrd
import os
import re



@transaction.atomic
def extractTrade(path=str):
    print('')
    
# Sample trade log xls: ./stocks/assets/sample.xls
class Command(BaseCommand):
    help = 'Extract trades from pnl sheets'
    print('test')
    worker_num = 10

    def add_arguments(self, parser):
        parser.add_argument('--ticker', nargs='?', type=str, help='tickers of the stocks to be imported')
        parser.add_argument('--all', action='store_true', default=False, help='import all stocks')


    def process(self):
        workbook = xlrd.open_workbook(r'./stocks/assets/sample.xls')
        worksheet = workbook.sheet_by_index(0)
        start_row = 3
        end_row = 26
        start_col = 1
        end_col = 25
        curr_row = start_row
        curr_col = start_col
        ticker = ''
        while curr_col < end_col:
            while curr_row < end_row:
                row = worksheet.row(curr_row)
                print('Row:{}'.format(curr_row))
                curr_cell = 0
                while curr_cell < 5:
                    # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
                    cell_type = worksheet.cell_type(curr_row, curr_col + curr_cell)
                    cell_value = worksheet.cell_value(curr_row, curr_col + curr_cell)
                    if cell_value != '':
                        print (' {} : {}'.format(cell_type,cell_value))
                    
                    curr_cell += 1
                curr_row += 1
            curr_col += 5


    def getFiles(self):
        files = []

        i = 0
        print(r"The following trade logs are available under F:\BaiduSync\trade\业绩单")
        for dirname, dirnames, filenames in os.walk(r'F:\BaiduSync\trade\业绩单'):
            #for subdirname in dirnames:
            #    print(os.path.join(dirname, subdirname))
                
            
            for filename in filenames:
                res = re.search("(.+)(\d{4}-\d{2}-\d{2})[\s+]?(.+).xls",filename)
                if res:
                    #trade = Trade()
                    i += 1
                    files.append(os.path.join(dirname, filename))
                    print(res.group(1))
        #print("Input the id of the file you want to import:")
        #selection = int(input())

    def handle(self, *args, **options):
        print(help)
        self.getFiles()
       
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


    