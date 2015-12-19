from stocks.models import *

import logging
from django.db.models import *
from stocks.transmodels.tradeset.TradeSet import TradeSet
import datetime



logger = logging.getLogger('stocks.services.TradeReportService')

class TradeReportService():

    def __init__(self):
        self.startDate = datetime.date.today()
        self.endDate = datetime.date.today()

    def setDate(self,date):
        self.startDate = date
        self.endDate = date

    def generateReport(self):
        #results = Trade.objects.filter(time__range = ['2015-07-01', '2015-11-01']).values('stock','time').annotate(net=Sum(F('price') * F('quantity')))['net']
        #results = Trade.objects.filter(time__range = ['2015-07-01', '2015-11-01']).extra(select={'commission': 'abs(price * quantity * 0.001)'}).values('commission','stock__ticker').annotate(net=Sum(ExpressionWrapper(F('price') * F('quantity')*-1, output_field = DecimalField(max_digits=15,decimal_places=3)))).order_by('net')
        #results = Trade.objects.raw('SELECT id,stock_id, SUM(price*quantity*-1-price*quantity*0.001) AS net FROM stocks_trade WHERE time BETWEEN %s and %s GROUP BY stock_id ORDER BY net DESC',['2015-07-01', '2015-11-01'])
        results = Trade.objects.filter(time__range = [self.startDate, self.endDate])
        
        self.buildTradeSet(results)

    def buildTradeSet(self, trades):
        if trades is None:
            return None
        tradeSet = TradeSet(trades)
        tradeSet.buildStockReport()

        
