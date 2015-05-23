from django.test import TestCase

from stocks.models import Stock,Tag

import json
import random
import time
import os

class StockTestCase(TestCase):
    fixtures = ['all-stocks.json']
    def setUp(self):
        self.createFiles()
        '''
        print("Loading haitong data...")
        fp = open('stocks/assets/haitong.csv')
        count = 0
        for line in fp:
            raw = line.split(',')
            count += 1
            #print(raw[1].rstrip())
            Stock.objects.create(name=raw[1].rstrip(), ticker=raw[0].rstrip()).save()
        print("Loading zxg data...")
        fp = open('stocks/assets/zxg.csv')
        count = 0
        for line in fp:
            raw = line.split(',')
            count += 1
            Stock.objects.create(name=raw[1].rstrip(), ticker=raw[0].rstrip()).save()
        '''
        
    def createFiles(self):

        print("Do you want to generate data from files?(y/n)")
        flag = input().rstrip()
        if("y"!=flag):
            return
        
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
        '''
        fp = open('stocks/assets/taglist.csv')
        count = 0
        data = []
        for line in fp:
            raw = line.split(',')
            count += 1
            Tag.objects.create(name=raw[0].rstrip()).save()
            obj = {
                "model": "stocks.Tag",
                "pk": count,
                "fields": {
                    "name": raw[0].rstrip()
                }
            }
            data.append(obj)
        fp.close()
        with open('stocks/fixtures/taglist.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile)
        '''
    
    def test_random_output(self):
        print("Test random stock...")
        flag = 'y'
        total = 7
        #book =  random.sample(list(Stock.objects.all()),100)
        book = list(Stock.objects.filter(rzrq=1))
        while flag == 'y' or flag == '1':
            sample = random.sample(book,total)
            while sample:
                hits = 0
                #data = []
                quit = False
                for stock in sample:
                    print(stock.name,end=': ')
                    start = time.time()
                    while(len(stock.ticker)<6):
                        stock.ticker = "0"+stock.ticker
                    token = input()
                    if stock.ticker == token:
                        end = time.time()
                        print(end-start)
                        hits += 1
                        continue
                    elif '000' == token:
                        quit = True
                        break
                        
                    else:
                        #data.append(stock)
                        print(stock.ticker)
    
                    #time.sleep(2)
                print('Hits: ', hits )
                if hits == total or quit==True:
                    quit = False
                    break
                #sample = random.sample(list(data),len(data))
                sample = random.sample(sample, total)
                
            
            print('Would you like another round?(y/n)')
            flag = input().rstrip()
        
