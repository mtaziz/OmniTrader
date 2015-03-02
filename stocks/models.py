from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=20)
    ticker = models.CharField(max_length=10)
    active = models.BooleanField(default=False)
    

class Tag(models.Model):
    name = models.CharField(max_length=50)
    stocks = models.ManyToManyField(Stock, through='StockTagRel')
    

class StockTagRel(models.Model):
    stock = models.ForeignKey(Stock)
    tag = models.ForeignKey(Tag)