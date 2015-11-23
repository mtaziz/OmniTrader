
from django.db import transaction
from stocks.models import *
import xlrd
import os
import re
from django.core.exceptions import ObjectDoesNotExist

class TradeRecordExtractor():
    def __init__(self,filename, tempfile):
        self.filename = filename
        self.tempfile = tempfile
        self.dry = True

    @transaction.atomic
    def process(self):
        res = re.search("(.+)(\d{4}-\d{2}-\d{2})[\s+]?(.+).xls",self.filename)
        if res:
            try:
                trader = Trader.objects.get(name=res.group(3))
                date = res.group(2)
                account = Account.objects.get(name=res.group(1))
            except ObjectDoesNotExist:
                print("Either the trader or account doesn't exist.")
                return 0
        else:
            print("Unable to extract information from {}".format(self.filename))
            return 0


        if TradeRecord.objects.filter(filename=self.filename,trader = trader,account = account, date = date).count()>0 :
            print("File {} has been loaded - skipped.".format(self.filename))
            return 0
            
        tradeRecord = TradeRecord(filename = self.filename, date = date, account = account, trader = trader)

        workbook = xlrd.open_workbook(self.tempfile)
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
                    trade = Trade(price=buy_price,quantity=buy_quant,stock=last_stock,trader=trader,account=account,time=date)
                    if self.dry != True:
                        #print("{} {}".format(buy_price,buy_quant))
                        trade.save()
                    count += 1
                if sell_price!='' and sell_quant!='' :
                    # mark quantity to negative as a sign of sell
                    trade = Trade(price=sell_price,quantity=0-sell_quant,stock=last_stock,trader=trader,account=account,time=date)
                    if self.dry != True:
                        trade.save()
                    count += 1

                curr_row += 1

            # reset start row and move to next column session
            curr_row = start_row
            curr_col += 5
        print("{} - {} trades saved.".format(self.filename, count))

        if self.dry != True:
            tradeRecord.save()
        return 1