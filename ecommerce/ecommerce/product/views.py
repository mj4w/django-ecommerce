from django.db import connection
from django.shortcuts import render
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from sqlparse import format

from .models import *
from .serializers import *


class CategoryView(viewsets.ViewSet):
    """
    A Simple Viewset for viewing categories
    """

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        queryset = Category.objects.all().isactive()
        serializer = CategorySerializer(
            queryset, many=True
        )  # many=true to define multiple categories
        return Response(serializer.data)


class BrandView(viewsets.ViewSet):
    """
    A Simple Viewset for viewing brand
    """

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        queryset = Brand.objects.all().isactive()
        serializer = BrandSerializer(
            queryset, many=True
        )  # many=true to define multiple categories
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):
    """
    A Simple Viewset for viewing product
    """

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        queryset = (
            Product.objects.filter(date_deleted__isnull=True).distinct().isactive()
        )
        serializer = ProductSerializer(
            queryset, many=True
        )  # many=true to define multiple categories
        return Response(serializer.data)

    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        queryset = (
            Product.objects.filter(slug=slug)
            .select_related("category", "brand")
            .isactive()
        )  # to filter all is_active=True
        serializer = ProductSerializer(
            queryset,
            many=True,
        )  # return the first object, as slug is unique

        data = Response(serializer.data)
        q = list(connection.queries)
        # print(len(q))
        """
         SQL Formatter allows to see the SQL Query formal in terminal
        """
        # print(len(q))
        for qs in q:
            sql_formatter = format(str(qs["sql"]), reindent=True)
            print(highlight(sql_formatter, SqlLexer(), TerminalFormatter()))
        return data

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<category_name>\w+)/all",
        url_name="all",
    )
    def list_category(self, request, category_name=None):
        """
        An endpoint to return products by category
        """
        queryset = Product.objects.filter(
            category__name__iexact=category_name
        ).isactive()  # to filter all is_active=True
        serializer = ProductSerializer(
            queryset,
            many=True,
        )  # using iexact for not case sensitive the category name

        return Response(serializer.data)

    @action(
        methods=["delete"],
        detail=False,
        url_path=r"delete/(?P<pk>[0-9]+)/",
    )
    @extend_schema(
        parameters=[
            {
                "name": "pk",
                "in": "path",
                "required": True,
                "schema": {
                    "type": "integer",
                },
            }
        ],
        responses={204: None, 404: None},
    )
    def delete_product(self, request, pk=None):
        """
        Delete a product
        """
        try:
            product = Product.objects.get(pk=pk, date_deleted__isnull=True)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product.date_deleted = timezone.now()
        product.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
