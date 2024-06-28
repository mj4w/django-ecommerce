from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *


class CategoryView(viewsets.ViewSet):
    """
    A Simple Viewset for viewing categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(
            self.queryset, many=True
        )  # many=true to define multiple categories
        return Response(serializer.data)


class BrandView(viewsets.ViewSet):
    """
    A Simple Viewset for viewing brand
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(
            self.queryset, many=True
        )  # many=true to define multiple categories
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):
    """
    A Simple Viewset for viewing product
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(
            self.queryset, many=True
        )  # many=true to define multiple categories
        return Response(serializer.data)
