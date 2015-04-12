from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Stock, Tag


def index(request):
    return HttpResponse("Hello, world. You're at the stocks index.")

def detail(request, stock_id):
    try:
        stock = Stock.objects.get(pk=stock_id)
    except Stock.DoesNotExist:
        raise Http404("Stock does not exist")
    return render(request, 'stocks/detail.html', {'stock': stock})


def tags(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        raise Http404("Tag does not exist")
    return render(request, 'tags/detail.html', {'tag': tag})

