from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from store.models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer, SameProductSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class PaginateProduct(PageNumberPagination):
    page_size = 4

class PaginateCollections(PageNumberPagination):
    page_size = 8

class DetailCollections(PageNumberPagination):
    page_size = 12


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    http_method_names = ['get']
    pagination_class = PaginateProduct   


    @action(detail=True)
    def similars(self, request, pk):
        """
        получить похожие продукты
        """
        product = self.get_object()
        collection = Collection.objects.get(id=product.colection.id)
        result = Product.objects.all().filter(colection_id=collection.id)[:5]
        serializer = SameProductSerializer(result, many=True)
        return Response(serializer.data)



class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    http_method_names = ['get']
    pagination_class = PaginateCollections


    @action(detail=True)
    def product(self, request, pk):
        """
        получить проддукты какой нибудь коллекции
        """

        pagination = PageNumberPagination()
        pagination.page_size = 12
        colection = self.get_object()
        products = Product.objects.all().filter(colection_id=colection.id)
        result = pagination.paginate_queryset(products, self.request)
        serializer = SameProductSerializer(result, many=True)
        return pagination.get_paginated_response(serializer.data)


    @action(detail=True)
    def new_prod(self, request, pk):
        """
        получить новинки
        """

        colection = self.get_object()
        products = Product.objects.all().filter(colection_id=colection.id).filter(new_prod=True)[:5]
        serializer = SameProductSerializer(products, many=True)
        return Response(serializer.data)








