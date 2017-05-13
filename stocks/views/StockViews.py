
from stocks.models import Stock
from rest_framework import generics, serializers,status
from rest_framework.response import Response
from taggit.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name', 'slug']

    def to_representation(self, obj):
        return obj.name

# Serializers define the API representation.
class StockSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Stock
        fields = ('name','ticker','tags')

# ViewSets define the view behavior.
class StockByTicker(generics.ListAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        ticker = self.kwargs['ticker']
        print(ticker)
        return Stock.objects.filter(ticker=ticker)


# ViewSets define the view behavior.
class StockByTags(generics.ListAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        if 'tags' not in self.request.query_params or self.request.query_params['tags'] == '':
            return
        # Split Chinese and English comma - replace Chinese comma with English comma first.
        tags = self.request.query_params['tags'].replace('，',',').split(',')
        queryset = None
        for tag in tags:
            if queryset is None:
                queryset = Stock.objects
            queryset = queryset.filter(tags__name__icontains=tag).distinct()
        return queryset
