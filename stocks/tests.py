from django.test import TestCase

from stocks.models import Stock

import xlrd

class StockTestCase(TestCase):
    def setUp(self):
        print("Setting up Stock tests...") 
        fp = open('stocks/assets/stocklist.csv')
        for line in fp:
            raw = line.split(',')
            if len(raw)>1:
                print(raw)
                Stock.objects.create(name=raw[1], ticker=raw[0].rstrip())
        fp.close()

    def test_stock(self):
        print("Test stock...")
        stock = Stock.objects.get(ticker="SH600030")
        print(stock.name)
        #self.assertEqual(stock.name, '600030')