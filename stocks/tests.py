from django.test import TestCase

from stocks.models import Stock,Tag

import json
import random
import time

class StockTestCase(TestCase):
    def setUp(self):
        print("Loading rzrq data...")
        fp = open('stocks/assets/rzrq.csv')
        count = 0
        for line in fp:
            raw = line.split(',')
            count += 1
            Stock.objects.create(name=raw[2].rstrip(), ticker=raw[1].rstrip()).save()
    '''
    def createFiles(self):
        data = []
        print("Setting up Stock tests...") 
        fp = open('stocks/assets/stocklist.csv')
        count = 0
        for line in fp:
            raw = line.split(',')
            if len(raw)>1:
                count += 1
                Stock.objects.create(name=raw[1].rstrip(), ticker=raw[0].rstrip()).save()
                obj = {
                    "model": "stocks.Stock",
                    "pk": count,
                    "fields": {
                        "name": raw[1].rstrip(),
                        "ticker": raw[0].rstrip()
                    }
                }
                data.append(obj)
        fp.close()
        with open('stocks/fixtures/stocklist.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile)

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
    
    '''    
    def test_stock(self):
        print("Test stock...")
        stock = Stock.objects.get(ticker="SH600030")
        print(stock.name)
        #self.assertEqual(stock.name, '600030')
    '''
    
    def test_random_output(self):
        print("Test random stock...")
        flag = 'y'
        while flag == 'y':
            sample = random.sample(list(Stock.objects.all()),10)
            hits = 0
            while sample:
                data = []
                for stock in sample:
                    print(stock.name,end=': ')
                    if stock.ticker == input() :
                        hits += 1
                        continue
                    else:
                        data.append(stock)
                        print(stock.ticker)
                        print()
    
                    #time.sleep(2)
                print('Hits: ', hits )
                sample = random.sample(list(data),len(data))
            
            print('Would you like another round?(y/n)')
            flag = input()
        
