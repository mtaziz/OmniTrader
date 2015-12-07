class DayTradeSet():
    def __init__(self, date):
        TradeSet.__init__(self)
        self.date = date
        self.tradeSetList = []
        
    def addTradeSet(self,tradeSet):
        self.tradeSetList.append(tradeSet)