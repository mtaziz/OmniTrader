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
            print(raw[2].rstrip().encode('utf8'))
            Stock.objects.create(name=raw[2].rstrip(), ticker=raw[1].rstrip()).save()
        '''
        print("Loading zxg data...")
        fp = open('stocks/assets/zxg.csv')
        count = 0
        for line in fp:
            raw = line.split(',')
            count += 1
            Stock.objects.create(name=raw[1].rstrip(), ticker=raw[0].rstrip()).save()
        '''
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
        total = 7
        book =  random.sample(list(Stock.objects.all()),100)
        while flag == 'y':
            sample = random.sample(book,total)
            while sample:
                hits = 0
                #data = []
                for stock in sample:
                    print(stock.name,end=': ')
                    start = time.time()
                    if stock.ticker == input() :
                        end = time.time()
                        print(end-start)
                        hits += 1
                        continue
                    else:
                        #data.append(stock)
                        print(stock.ticker)
    
                    #time.sleep(2)
                print('Hits: ', hits )
                if hits == total:
                    break
                #sample = random.sample(list(data),len(data))
                sample = random.sample(sample, total)
                
            
            print('Would you like another round?(y/n)')
            flag = input().rstrip()
        
