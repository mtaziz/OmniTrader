from django.core.management.base import BaseCommand, CommandError
from stocks.models import Stock, DayData
from django.db import transaction

import json
import random
import time
import os
import csv
import datetime

# sample csv file
#代码	    名称	    现价	    总手	        开盘	    最高  	最低
#SZ000001	平安银行	12.54	67964257	12.61	12.69	12.45
#SZ000002	万  科Ａ	14.76	127326271	14.78	14.82	14.57

# This script is a command tool for loading EOD data of a specific day from a csv file
# Usage: 
# 1. export the EOD data from TongHuaShun and save as csv(original generated file is in wrong format)
# 2. change the date in the code
# 3. run this command
class Command(BaseCommand):
    help = 'Load single day data from csv exported from TongHuaShun'

    def add_arguments(self, parser):
        return

    def handle(self, *args, **options):
        self.exportFromFile(r'C:\Users\Andrew\Desktop\20150817.csv')

    @transaction.atomic
    def exportFromFile(self, path:str):
        with open(path) as csvfile:
            data  = csv.reader(csvfile,delimiter = ',')
            header = next(data)
            print(header)
            for row in data:
                ticker=row[0][2:].strip()
                try:
                    #print(ticker)
                    date = datetime.date(2015,8,17)
                    stock = Stock.objects.get(ticker=ticker)
                    if DayData.objects.filter(stock=stock, date=date).exists():
                        #record exists, skip
                        print('{} - {} - {} - {} - {} - {} - {}'.format(stock.ticker,stock.name,row[2],row[3],row[4],row[5],row[6]))
                    else:
                        if row[3].isdigit() and int(row[3]) > 0:
                            obj = DayData(stock=stock,date=date,open=row[4],high=row[5],low=row[6],close=row[2],volume=row[3])
                            obj.save()
                            print('{}({}) {} saved.'.format(stock.name,stock.ticker, date))
                        else:
                            print('{}({}) suspended on {} - skipped.'.format(stock.name,stock.ticker, date))
                except Stock.DoesNotExist:
                    print('Stock not found : {}'.format(ticker))