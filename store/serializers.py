from dataclasses import field
from rest_framework import serializers
from store.models import Callback, Collection, Collection, Image, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('colection', 'name', 'articul', 'price', 'final_price', 'sales', 
                  'description', 'size', 'composition', 'stock', 'material', 'favorite')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerialiser(instance.images.all(), many=True, context=self.context).data
        representation['colection'] = instance.colection.name
        return representation   
        

class ProductImageSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'color')


class SameProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'final_price', 'price', 'sales', 'size', 'favorite', 'images', 'colection')

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['images'] = ProductImageSerialiser(instance.images.all(), many=True, context=self.context).data
        
        return representation

    
class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__' 
        

class CallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Callback
        fields = '__all__'