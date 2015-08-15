from django.core.management.base import BaseCommand, CommandError
from stocks.models import Stock, DayData


import json
import random
import time
import os

class Command(BaseCommand):
    help = 'Create Json data from csv'

    def add_arguments(self, parser):
        parser.add_argument('--ticker', nargs='?', type=str, help='tickers of the stocks to be imported')

    def handle(self, *args, **options):
        files = []

        i = 0
        print("The following csv files are available under stocks/assets")
        for dirname, dirnames, filenames in os.walk('./stocks/assets'):
            #for subdirname in dirnames:
            #    print(os.path.join(dirname, subdirname))
                
            
            for filename in filenames:
                if filename.endswith(".csv"):
                    i += 1
                    files.append(os.path.join(dirname, filename))
                    print("{}. {}".format(i,filename))
        print("Input the id of the file you want to import:")
        selection = int(input())
        
        if selection > i or selection <=0:
            print("Selection out of range.")
            return
            
        
        print("Input the column index of the ticker(start from 0):")
        ticker_col = int(input())
        
        print("Input the column index of the name(start from 0):")
        name_col = int(input())


        print("Input the column index of the rzrq indicator(start from 0):")
        rzrq_col = int(input())
        
        print("Input the output filename(end with .json):")
        output = input()
        
        print("Generating Json file from {}...".format(files[selection-1]))

        data = []
        fp = open(files[selection-1])
        count = 0
        for line in fp:
            raw = line.split(',')
            if len(raw)>1:
                count += 1
                rzrq_flag = False if raw[rzrq_col].rstrip()=="" else True
                #Stock.objects.create(name=raw[name_col].rstrip(), ticker=raw[ticker_col].rstrip(), rzrq=rzrq_flag).save()
                obj = {
                    "model": "stocks.Stock",
                    "pk": count,
                    "fields": {
                        "name": raw[name_col].rstrip(),
                        "ticker": raw[ticker_col].rstrip(),
                        "rzrq": rzrq_flag
                    }
                }
                data.append(obj)
        fp.close()
        print("{} stocks recorded".format(count))
        with open("stocks/fixtures/{}".format(output), 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile)


    