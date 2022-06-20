from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from main.models import Slider
from main.serializer import SliderSerializer
from store.models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer, SameProductSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class PaginateProduct(PageNumberPagination):
    page_size = 3

class PaginateCollections(PageNumberPagination):
    page_size = 8

class DetailCollections(PageNumberPagination):
    page_size = 12

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    pagination_class = PaginateProduct   


class CollectionAPIView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = PaginateCollections


class PerviosAPIVew(generics.ListAPIView):
    # slider = Slider.objects.all()
    queryset = Collection.objects.all().order_by()[:4]
    # prods = Product.objects.all().order_by()[:4]

    serializer_class = CollectionSerializer

class CollectionDetailAPIWiew(generics.ListAPIView):
    queryset = Product.objects.all()


    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(colection_id=kwargs['pk'])
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response(serializer.data)

    serializer_class = SameProductSerializer
    pagination_class = PaginateProduct