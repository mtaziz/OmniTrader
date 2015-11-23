from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import *
from django.http.response import JsonResponse
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    #return HttpResponse("Hello, world. You're at the stocks index.")
    return render(request, 'general/base.html', {})



def detail(request, stock_ticker):
    try:
        stock = Stock.objects.get(ticker=stock_ticker)
    except Stock.DoesNotExist:
        raise Http404("Stock does not exist")
    return render(request, 'stocks/detail.html', {'stock': stock})


def tags(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        raise Http404("Tag does not exist")
    return render(request, 'tags/detail.html', {'tag': tag})


def attachtag(request, stock_ticker):

    try:
        stock = Stock.objects.get(ticker=stock_ticker)

    except Stock.DoesNotExist:
        raise Http404("Stock does not exist")
    
    if request.method == 'POST':
        try:
            tag = Tag.objects.get(pk=1)
            #tag.stocks.add(stock)
            #tag.save()
        except Tag.DoesNotExist:
            raise Http404("Tag does not exist")
        return render(request, 'stocks/detail.html', {'stock': stock})
    else:
        return render(request, 'stocks/attachtag.html', {'stock': stock})
    
def dayData(request, stock_ticker):
    return render(request, 'stocks/daydata.html',{'ticker': stock_ticker})

def getDayData(request, stock_ticker):
    try:
        stock = Stock.objects.get(ticker=stock_ticker)
        #print(DayData.objects.filter(stock=stock).values())
        raw = list(DayData.objects.filter(stock=stock,volume__gt=0).values())
        return JsonResponse({'data':json.dumps(raw,cls=DjangoJSONEncoder)})

    except Stock.DoesNotExist:
        raise Http404("Stock does not exist")
    
def trades(request, date):
    try:
        trades = Trade.objects.filter(time=date)
    except Trade.DoesNotExist:
        raise Http404("Trades does not exist")
    return render(request, 'trades/detail.html', {'trades': trades})