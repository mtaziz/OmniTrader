from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=20)
    ticker = models.CharField(max_length=10,db_index=True)
    rzrq = models.BooleanField(default=False)
    

class Tag(models.Model):
    name = models.CharField(max_length=50)
    stocks = models.ManyToManyField(Stock, through='StockTagRel')
    

class StockTagRel(models.Model):
    stock = models.ForeignKey(Stock)
    tag = models.ForeignKey(Tag)

class DayData(models.Model):
    stock = models.ForeignKey(Stock, related_name='dayHist')
    date = models.DateField()
    # blank for validation while null for db storage
    open = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    close = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    high = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    low = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    adj_open = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    adj_close = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    adj_high = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    adj_low = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    volume = models.IntegerField()

    class Meta:
        index_together = ['stock','date'] 
        unique_together = ('stock', 'date')
        
class Account(models.Model):
    name = models.CharField(max_length=127)

class Trader(models.Model):
    name = models.CharField(max_length=127)

class Trade(models.Model):
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.IntegerField()
    stock = models.ForeignKey(Stock, related_name='trades')
    trader = models.ForeignKey(Trader, related_name='trades',blank=True, null=True)
    account = models.ForeignKey(Account, related_name='trades',blank=True, null=True)
    time = models.DateField(blank=True,null=True)
    comment = models.TextField(blank=True,null=True)

class TradeRecord(models.Model):
    filename = models.CharField(max_length=127)
    account = models.ForeignKey(Account, related_name='recordfiles')
    trader = models.ForeignKey(Trader, related_name='recordfiles')
    date = models.DateField()
