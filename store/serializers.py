from rest_framework import serializers
from store.models import Callback, Cart, Collection, Image, Product, Order, CartItem


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализация продуктов """
    class Meta:
        model = Product
        fields = ('colection', 'name', 'articul', 'price', 'final_price', 'sales', 
                  'description', 'size', 'composition', 'stock', 'material', 'favorite')

    """ данный метод отвечает за представление изборажений и коллекций """
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerialiser(instance.images.all(), many=True, context=self.context).data
        representation['colection'] = instance.colection.name
        return representation   
        

class ProductImageSerialiser(serializers.ModelSerializer):
    """ Сериализация изображений """
    class Meta:
        model = Image
        fields = ('image', 'color')


class SameProductSerializer(serializers.ModelSerializer):
    """ Сериализация подпродуктов """
    class Meta:
        model = Product
        fields = ('id', 'name', 'final_price', 'price', 'sales', 'size', 'favorite', 'images', 'colection')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerialiser(instance.images.all(), many=True, context=self.context).data
        
        return representation

    
class CollectionSerializer(serializers.ModelSerializer):
    """ Сериализация коллекций """
    class Meta:
        model = Collection
        fields = '__all__' 
        

class CallbackSerializer(serializers.ModelSerializer):
    """ Сериализация Обратного звонка """
    class Meta:
        model = Callback
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    """ Сериализация корзины """
    class Meta:
        model = Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """ Сериализация Заказа """
    class Meta:
        model = Order
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


