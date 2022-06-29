from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, generics

from main.models import AboutUs, Advantage, Footer, Help, News, Offerta, Slider
from main.serializer import AboutUsSerializer, AdvantageSerializer, FooterSerializer, HelpSerializer, NewsSerializer, OffertaSerializer, SliderSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class NewsPaginate(PageNumberPagination):
    page_size = 8


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    http_method_names = ['get']


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


class FooterViewSet(viewsets.ModelViewSet):

    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

    http_method_names = ['get']


class AdvatageViewSet(viewsets.ModelViewSet):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer
    http_method_names = ['get']

