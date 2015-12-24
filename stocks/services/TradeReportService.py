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

    def setDate(self,startdate, enddate):
        self.startDate = startdate
        self.endDate = enddate

    def generateReport(self):
        results = Trade.objects.filter(time__range = [self.startDate, self.endDate])
        if results is None:
            return None
        tradeSet = TradeSet(results)
        tradeSet.buildStockReport()

        

        
