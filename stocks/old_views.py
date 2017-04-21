from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import *
from django.http.response import JsonResponse
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import logging
import tushare
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt
from datetime import date

logger = logging.getLogger('stocks.views')

def index(request):
    #return HttpResponse("Hello, world. You're at the stocks index.")
    return render(request, 'general/base.html', {})



def detail(request, stock_ticker):
    try:
        stock = Stock.objects.get(ticker=stock_ticker)
    except Stock.DoesNotExist:
        raise Http404("Stock does not exist")
    return render(request, 'stocks/detail.html', {'stock': stock})

'''
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

'''
def dayData(request, stock_ticker):
    return render(request, 'stocks/daydata.html',{'ticker': stock_ticker})

def getDayData(request, stock_ticker):
    try:
        #Old way, replaced with tushare
        #stock = Stock.objects.get(ticker=stock_ticker)
        #raw = list(DayData.objects.filter(stock=stock,volume__gt=0).values())
        #return JsonResponse({'data':json.dumps(raw,cls=DjangoJSONEncoder)})
        # data frame must be sorted in asc order so that amchart could visualise it.
        res = tushare.get_hist_data(stock_ticker).sort_index(ascending=True)
        res['date'] = res.index
        return JsonResponse({'data':res.to_json(orient='records')})
    except Stock.DoesNotExist:
        raise Http404("Stock does not exist")
    
def trades(request, date):
    try:
        trades = Trade.objects.filter(time=date)
    except Trade.DoesNotExist:
        raise Http404("Trades does not exist")
    return render(request, 'trades/detail.html', {'trades': trades})

def report(request):
    startDate = request.GET.get('startdate',date(1970,1,1))
    endDate = request.GET.get('enddate', date.today())
    raw = Trade.objects.filter(time__range=[startDate,endDate])
    if request.GET.get('accountid',None) is not None:
        raw = raw.filter(account__id=request.GET['accountid'])
    if request.GET.get('stockid',None) is not None:
        raw = raw.filter(stock__id=request.GET['stockid'])
    return JsonResponse({'data':json.dumps(list(raw.values()),cls=DjangoJSONEncoder)})


@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        logger.info("Receiving challenge : {}".format(request.GET['challenge']))
        return HttpResponse(request.GET['challenge'])
    elif request.method == 'POST':
        logger.info("Receiving notification from Dropbox")
        #TODO: run in different thread and deal with concurrency
        #call_command('readDropBox')
        #logger.info('Command is running...')
        return HttpResponse('')