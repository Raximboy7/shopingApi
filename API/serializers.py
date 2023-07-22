from rest_framework import serializers
from .models import Category, Product, Buy


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('slug', 'name', 'img')


class ProductSerializer(serializers.ModelSerializer):
    slug = CategorySerializer()
    class Meta:
        model = Product
        fields = ('slug', 'title', 'price', 'description', 'quantity')


class BuySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Buy
        fields = ('quantity', 'phone', 'product')
