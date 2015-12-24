
from stocks.transmodels.tradeset.StockDayTradeSet import StockDayTradeSet
class StockTradeSet():
    def __init__(self, stock):
        self.stock = stock
        self.tradeDict = {}
        self.net = 0
        self.volume = 0
        self.efficiency = 0
        
    def addTrade(self,trade):
        if trade is None:
            return
        if trade.time in self.tradeDict:
            self.tradeDict[trade.time].addTrade(trade)
        else:
            self.tradeDict[trade.time] = StockDayTradeSet(trade.stock,trade.time).addTrade(trade)
        return self

    def calculate(self):
        self.net = 0
        self.volume = 0
        for dayTradeSet in self.tradeDict.values():
            dayTradeSet.calculate()
            # Decide to ignore overnight position net - meaningless
            if dayTradeSet.positionClosed:
                self.net += dayTradeSet.net
                self.volume += dayTradeSet.volume
        if self.volume > 0:
            self.efficiency = self.net / self.volume
