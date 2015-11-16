from django.contrib import admin
from stocks.models import *

class StockAdmin(admin.ModelAdmin):
    list_display = ['ticker','name']
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class TraderAdmin(admin.ModelAdmin):
    list_display = ['name']
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name']
class TradeAdmin(admin.ModelAdmin):
    list_display = ['id','time','stock_link','price','quantity','comment']
    def stock_link(self, obj):
        return obj.stock.ticker
    stock_link.allow_tags = True

# Register your models here.
admin.site.register(Stock, StockAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(StockTagRel)
admin.site.register(DayData)
admin.site.register(Trader,TraderAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Trade,TradeAdmin)