from django.urls import path
from main.views import *
from .views import CallbackViewSet, CollectionViewSet, FavoriteViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'slider', SliderViewSet, basename='slider')
router.register(r'collection', CollectionViewSet, basename='collection')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'about_us', AboutUsViewSet, basename='about_us')
router.register(r'offerta', OffertaViewSet, basename='offerta')
router.register(r'help', HelpViewSet, basename='help')
router.register(r'footer', FooterViewSet, basename='footer')
router.register(r'advantage', AdvatageViewSet, basename='advantage')
router.register(r'callback', CallbackViewSet, basename='callback')
router.register(r'favorite', FavoriteViewSet, basename='favorite')


urlpatterns = [

              ] + router.urls
