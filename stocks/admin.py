from django.contrib import admin
from stocks.models import Stock,Tag,StockTagRel

# Register your models here.
admin.site.register(Stock)
admin.site.register(Tag)
admin.site.register(StockTagRel)