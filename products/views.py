from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import  Product
from .serializers import ProductSerializer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.pagination import PageNumberPagination



class ProductPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
