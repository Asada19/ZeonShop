from django.urls import path
from main.views import AboutUsViewSet, HelpViewSet, NewsViewSet, OffertaViewSet

from store.models import Collection, Product 
from .views import CollectionViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

# product_detail = ProductViewSet.as_view({'get': 'retrieve'})
# collection_detail = CollectionViewSet.as_view({'get': 'retrieve'})
# news_detail = NewsViewSet.as_view({'get': 'retrieve'})
# collection_prod = CollectionViewSet.product(Collection.objects.all())
router = DefaultRouter()
router.register(r'collection', CollectionViewSet, basename='collection')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'about_us', AboutUsViewSet, basename='about_us')
router.register(r'offerta', OffertaViewSet, basename='offerta')
router.register(r'help', HelpViewSet, basename='help')


urlpatterns = [
    # path('products/', ProductViewSet.as_view({'get': 'list'})),
    # path('products/<int:pk>/', product_detail, name='product_detail'),
] + router.urls

