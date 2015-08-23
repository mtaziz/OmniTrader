from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Stock, Tag, DayData
from django.http.response import JsonResponse
import json
from django.core import serializers


def index(request):
    return HttpResponse("Hello, world. You're at the stocks index.")


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
    
def getDayData(request, stock_ticker):
    try:
        stock = Stock.objects.get(ticker=stock_ticker)
        data = serializers.serialize('json',DayData.objects.filter(stock=stock))
        return JsonResponse({'data':data})

    except Stock.DoesNotExist:
        raise Http404("Stock does not exist")
    
        