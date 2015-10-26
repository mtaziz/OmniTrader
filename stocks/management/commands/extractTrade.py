from django.core.management.base import BaseCommand, CommandError

from django.db import transaction
from stocks.models import Trade,Trader,Account,Stock
import xlrd
import os
import re
from math import log10



@transaction.atomic
def extractTrade(path=str):
    print('')
    
# Sample trade log xls: ./stocks/assets/sample.xls
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--dir', nargs='?', type=str, help='directories of trade logs')
        parser.add_argument('--acct', nargs='?', type=int, help='specify account id')
        parser.add_argument('--date', nargs='?', type=str, help='specify the date to load')
        parser.add_argument('--dry', action='store_true', default=False, help='dry run if true')


    @transaction.atomic
    def process(self, dirname, filename, dry, account, trader, time):
        
        workbook = xlrd.open_workbook(os.path.join(dirname, filename))
        worksheet = workbook.sheet_by_index(0)
        start_row = 3
        end_row = 26
        start_col = 1
        end_col = 25
        curr_row = start_row
        curr_col = start_col
        count = 0
        last_stock = None
        while curr_col < end_col:
            while curr_row < end_row:
                row = worksheet.row(curr_row)

                # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
                buy_quant = worksheet.cell_value(curr_row, curr_col)
                buy_price = worksheet.cell_value(curr_row, curr_col + 1)
                sell_quant = worksheet.cell_value(curr_row, curr_col + 3)
                sell_price = worksheet.cell_value(curr_row, curr_col + 4)
                #cell_type = worksheet.cell_type(curr_row, curr_col + curr_cell)
                #cell_value = worksheet.cell_value(curr_row, curr_col + curr_cell)
                if worksheet.cell_value(curr_row, curr_col + 2)!='':
                    ticker = int(worksheet.cell_value(curr_row, curr_col + 2))
                    # quick fix to get Shenzhen stock ticker(add missing zeroes as prefix)
                    if ticker<100000:
                        ticker = "000000"[(int(log10(ticker))+1):]+str(ticker)
                    last_stock = Stock.objects.get(ticker = str(ticker))

                    
                    
                if buy_price!='' and buy_quant!='' :
                    trade = Trade(price=buy_price,quantity=buy_quant,stock=last_stock,trader=trader,account=account,time=time)
                    if dry != True:
                        trade.save()
                    count += 1
                if sell_price!='' and sell_quant!='' :
                    # mark quantity to negative as a sign of sell
                    trade = Trade(price=sell_price,quantity=0-sell_quant,stock=last_stock,trader=trader,account=account,time=time)
                    if dry != True:
                        trade.save()
                    count += 1

                curr_row += 1

            # reset start row and move to next column session
            curr_row = start_row
            curr_col += 5
        print("{} - {} trades saved.".format(filename, count))
        return 1

        

    def handle(self, *args, **options):
        dir = r'F:\BaiduSync\trade\业绩单'
        dry = False
        acct = None
        date = None
        if options['dir']!=None:
            dir = options['dir']
        print('Start to extract and save trade logs under {}'.format(dir))
        if options['acct']!=None:
            acct = Account.objects.get(id=options['acct'])
            print('Only looking at account {}'.format(acct.name))
        if options['date']!=None:
            date = options['date']
            print('Load date {}'.format(date))
        if options['dry']==True:
            dry = True
            print('Performing dry run')

        i = 0
        for dirname, dirnames, filenames in os.walk(r'F:\BaiduSync\trade\业绩单'):
            
            for filename in filenames:
                res = re.search("(.+)(\d{4}-\d{2}-\d{2})[\s+]?(.+).xls",filename)
                if res:
                    trader = None
                    account = None
                    time = None
                    trader = Trader.objects.get(name=res.group(3))
                    time = res.group(2)
                    account = Account.objects.get(name=res.group(1))
                    # Skip the unspecified accounts and dates
                    if acct!=None and account != acct:
                        continue
                    if date!=None and time !=date:
                        continue
                    i += self.process(dirname, filename, dry, acct, trader, date)

        print("{} trade logs extracted.".format(i))


        return



    