from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="name")

    class Meta:
        model = Category
        fields = ["category_name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductLine
        exclude = ("id", "product", "is_active")


class ProductSerializer(serializers.ModelSerializer):

    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source="category.name")
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "description",
            "brand_name",
            "date_deleted",
            "category_name",
            "product_line",
        )
