from rest_framework import serializers
from .models import Product, reviews, Category

class CategorySerial(serializers.ModelSerializer):
    category_name=serializers.CharField(source='name')
    class Meta:
        model= Category
        fields=['id', 'category_name']
class ReviewSerial(serializers.ModelSerializer):
    class Meta:
        model= reviews
        fields=['id','product','user','rating']
    read_fields= ['product','user']

class ProductSerial(serializers.ModelSerializer):
    product_name=serializers.CharField(source='name')
    class Meta:
        model= Product
        fields = ['id', 'product_name', 'price', 'Category', 'isActiv']
