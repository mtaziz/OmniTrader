from django.test import TestCase

from stocks.models import Stock

import json
import random
import time

class StockTestCase(TestCase):
    def setUp(self):
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
        
        '''
        with open('stocks/fixtures/stocklist.json', 'w', encoding='utf-8') as outfile:
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

        sample = random.sample(list(Stock.objects.all()),50)
        for stock in sample:
            print(stock.ticker, stock.name)
            time.sleep(2)
