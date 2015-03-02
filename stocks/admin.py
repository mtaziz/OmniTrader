from django.contrib import admin
from stocks.models import Stock,Tag,StockTagRel

class StockAdmin(admin.ModelAdmin):
    list_display = ['ticker','name']
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Stock, StockAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(StockTagRel)