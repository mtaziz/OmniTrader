
class StockDayTradeSet():
    def __init__(self, stock, date):
        self.stock = stock
        self.date = date
        self.trades = []
        self.net = 0
        self.efficiency = 0
        self.volume = 0
        self.position = 0
        self.positionClosed = False
        
    def addTrade(self,trade):
        self.trades.append(trade)
        return self

    def calculate(self):
        for trade in self.trades:
            self.position += trade.quantity
            if trade.quantity > 0:
                self.net -= trade.quantity * float(trade.price) * 1.0005
            else:
                self.net -= trade.quantity * float(trade.price) * 0.9985
            if trade.quantity < 0:
                self.volume -= trade.quantity * float(trade.price)
        # Day trade - calculate efficiency
        if self.position < 100 and self.position > -100:
            self.positionClosed = True
            self.efficiency = self.net / self.volume
        return