from django.contrib import admin
from stocks.models import *

class StockAdmin(admin.ModelAdmin):
    list_display = ['ticker','name']

#class TagAdmin(admin.ModelAdmin):
#    list_display = ['name']

class TraderAdmin(admin.ModelAdmin):
    list_display = ['name']
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name']
class TradeAdmin(admin.ModelAdmin):
    #Add to optimize long ttfb problem
    #(around 2000 dup sqls without this and 40 secs for the page to load)
    list_select_related = True
    list_select_related = ('account', 'stock')
    list_display = ['id','time','stock_link','price','quantity','account_link','comment']
    readonly_fields = ('stock','account','trader')
    search_fields = ('time','stock__ticker')
    list_filter = ('time',)
    def account_link(self, obj):
        return obj.account.name
    def stock_link(self, obj):
        return obj.stock.ticker+' '+obj.stock.name
    stock_link.allow_tags = True
    ordering = ('-time',)
# Register your models here.
admin.site.register(Stock, StockAdmin)
#admin.site.register(Tag, TagAdmin)
#admin.site.register(StockTagRel)
admin.site.register(DayData)
admin.site.register(Trader,TraderAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Trade,TradeAdmin)
