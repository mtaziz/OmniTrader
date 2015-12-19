from stocks.models import *
from stocks.transmodels.tradeset.StockTradeSet import StockTradeSet
import datetime

class TradeSet():
    def __init__(self, trades):
        self.trades = trades
        self.tradeDict = {}
        self.net = 0
        self.efficiency = 0
        self.volume = 0
        
    def buildStockReport(self):
        for trade in self.trades:
            if trade.stock in self.tradeDict:
                self.tradeDict[trade.stock].addTrade(trade)
            else:
                self.tradeDict[trade.stock] = StockTradeSet(trade.stock).addTrade(trade)
        self.calculate()
        print("net {}, efficiency {}".format( self.net, self.efficiency))

    def calculate(self):
        self.net = 0
        self.efficiency = 0
        self.volume = 0
        for tradeSet in self.tradeDict.values():
            tradeSet.calculate()
            self.net += tradeSet.net
            self.volume += tradeSet.volume
        self.efficiency = self.net / self.volume
            
        