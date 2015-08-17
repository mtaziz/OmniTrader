from django.core.management.base import BaseCommand, CommandError
from stocks.models import Stock, DayData
from django.db import transaction

import json
import random
import time
import os
import csv

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
                    stock = Stock.objects.get(ticker=ticker)
                    print('{} - {} - {} - {} - {} - {} - {}'.format(stock.ticker,stock.name,row[2],row[3],row[4],row[5],row[6]))
                    #print(stock.name)
                except Stock.DoesNotExist:
                    print('Not found : {}'.format(ticker))