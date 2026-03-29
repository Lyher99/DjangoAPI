from rest_framework import generics
from django.shortcuts import render

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


def home(request):
	return render(request, 'index.html')


class CategoriesListCreate(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class CategoriesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class ProductsListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
