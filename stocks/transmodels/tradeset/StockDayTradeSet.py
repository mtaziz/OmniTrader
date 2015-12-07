
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

    def calculate(self):
        for trade in self.trades:
            self.position += trade.quantity
            if trade.quantity>0:
                self.net -= trade.quantity * trade.price * 1.001
            else:
                self.net -= trade.quantity * trade.price * 0.99
            if trade.quantity <0:
                self.volume -= trade.quantity * trade.price
        # Day trade - calculate efficiency
        if self.position<100 and self.position>-100:
            self.positionClosed = True
            self.efficiency = self.net / self.volume
        return