
class StockTradeSet():
    def __init__(self, stock):
        self.stock = stock
        self.tradeSetList = []
        
    def addTradeSet(self,tradeSet):
        self.tradeSetList.append(tradeSet)