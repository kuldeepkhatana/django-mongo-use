from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

from odata.models import Product, Customer
from odata.serializers import ProductSerializers
from rest_framework import viewsets
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    """ This viewset is used for crud operations"""
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers    