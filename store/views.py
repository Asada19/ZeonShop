import random
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework import viewsets, generics
from store.forms import CallbackForm
from store.models import Callback, Collection, Product
from .serializers import CallbackSerializer, CollectionSerializer, ProductSerializer, SameProductSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.
"""Глобальная функция рандома"""


def get_random_objects(massiv, count) -> list:
    # colect = set(Collection.objects.all())
    # prods = set(Product.objects.filter(collect='collection'))
    # some_data = [{colect : prods for collect, prods in }]
    data = set(massiv.objects.all())
    res = [random.sample(data, count)][0]
    return res


class PaginateProduct(PageNumberPagination):
    page_size = 8


class PaginateCollections(PageNumberPagination):
    page_size = 8


class DetailCollections(PageNumberPagination):
    page_size = 12


class ProductViewSet(viewsets.ModelViewSet):
    ''' bla bla'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post']
    pagination_class = PaginateProduct

    @action(detail=True, methods=['get'])
    def similars(self, request, pk):
        """
        получить похожие продукты
        """
        product = self.get_object()
        collection = Collection.objects.get(id=product.colection.id)
        result = Product.objects.all().filter(colection_id=collection.id)[:5]
        serializer = SameProductSerializer(result, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])  # router builds path posts/search/?q=word
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(name__icontains=q))
        serializer = SameProductSerializer(queryset, many=True)
        if not queryset:  # если объект поиска не был найден
            new_list = Collection.objects.all()
            if new_list.count() >= 5:
                collection = random.sample(list(new_list), 5)
            else:
                collection = new_list
            random_collections = []
            if not queryset or collection:
                for i in collection:
                    if i.colection.all():  # проверка - есть ли что то в данной коллекции
                        random_collections.append({'key': i.colection.all()})
                random_prod = []
                for i in random_collections:
                    random_prod.append(random.choice(list(i['key'])))
                queryset = random_prod
                if len(random_prod) > 5:
                    queryset = random_prod[:5]
            else:
                page = self.paginate_queryset(queryset)
                if page is not None:
                    serializer = self.get_serializer(page, many=True)
                    return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True, )
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk):
        product = self.get_object()
        if product.favorite == False:
            product.favorite = True
        else:
            product.favorite = False
        product.save()
        serializer = SameProductSerializer(product)
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
        products = Product.objects.all().filter(colection_id=colection.id) | Product.objects.all().filter(
            new_prod=True)[:5]
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


class CallbackViewSet(viewsets.ModelViewSet):
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer
    http_method_names = ['get', 'post']


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(favorite=True)
    serializer_class = SameProductSerializer
    pagination_class = DetailCollections
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all().filter(favorite=True)
        serializer = SameProductSerializer(queryset, many=True)
        random_prod = []
        if not queryset:
            new_list = Collection.objects.all()
            collection = random.sample(list(new_list), 5)
            random_collections = []
            for i in collection:
                random_collections.append({'key': i.colection.all()})
            for i in random_collections:
                random_prod.append(random.choice(list(i['key'])))
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
