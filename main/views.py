from django.shortcuts import render
from rest_framework import viewsets

from main.models import AboutUs, Help, News, Offerta
from main.serializer import AboutUsSerializer, HelpSerializer, NewsSerializer, OffertaSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class NewsPaginate(PageNumberPagination):
    page_size = 8


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['get']
    pagination_class = NewsPaginate


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    http_method_names = ['get']


class OffertaViewSet(viewsets.ModelViewSet):
    queryset = Offerta.objects.all()
    serializer_class = OffertaSerializer
    http_method_names = ['get']


class HelpViewSet(viewsets.ModelViewSet):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
    http_method_names = ['get']
    