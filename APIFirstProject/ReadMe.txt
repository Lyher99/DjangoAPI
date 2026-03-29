create project api in django


1. Create Django Project

pip install --user virtualenv

python -m virtualenv env
cd env
cd Scripts
activate
cd..
cd..

pip install Django

django-admin startproject APIFirstProject

cd APIFirstProject

python manage.py runserver

http://127.0.0.1:8000/

ctrl + c = stop service

code . = open vs code

python manage.py startapp AppAPI

2. Register App In APIFirstProject/settings.py:



Add it to your environment:

INSTALLED_APPS = [
    ...
    'AppAPI',
]

3. Create Model In AppAPI/models.py:

from django.db import models

class Category(models.Model):
    categoryName = models.CharField(max_length=200, null=True)
    categoryImage = models.ImageField(upload_to='images/Categories/', null=True, blank=True)

    def __str__(self):         
        return self.categoryName

class Product(models.Model):
    productName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=200, null=True)
    productDescript = RichTextUploadingField(null=True)
    weight = models.CharField(max_length=200, null=True)
    availability = models.CharField(max_length=200, null=True)
    shipping = models.CharField(max_length=200, null=True)
    productImage = models.ImageField(upload_to='images/Products/', null=True, blank=True)
    productDate = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):         
        return self.productName

----

pip install django-ckeditor

INSTALLED_APPS = [
     'ckeditor',
]

models.py:

from ckeditor_uploader.fields import RichTextUploadingField


CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'all',
        'skin':'moono',
        'codeSnippet_theme':'monokai',
        'extraPlugins':','.join(
            [
                'codesnippet',
                'widget',
                'dialog'
            ]
        )
    },
}

import os

STATIC_URL = 'static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS =[
    BASE_DIR / 'static/',
]

from django.conf import settings
from django.conf.urls.static import static

+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Run migrations:

python -m pip install Pillow

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

Admin:

from .models import *

admin.site.register(Category)
admin.site.register(Product)


Install Django REST Framework

pip install django djangorestframework


INSTALLED_APPS = [    
'rest_framework',
]




Create File serializers.py in App api

from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:        
	model = Product
        fields = ['id', 'productName', 'price','productImage','productDate']


AppAPI/views.py:

from rest_framework import generics
from .serializers import ProductSerializer

# Create your views here.

# ListCreateAPIView provides GET (list) and POST (create) actions 

class ProductsListCreate(generics.ListCreateAPIView):
   	queryset = Product.objects.all()    
  	serializer_class = ProductSerializer

# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions

class ProductsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):    
	queryset = Product.objects.all()
    	serializer_class = ProductSerializer


Create URL AppAPI/urls.py: 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer)
]

from .views import * 
 
urlpatterns = [
    path('APIProduct/', ProductsListCreate.as_view(), name='APILCProduct'),
 
    path('APIProduct/<int:pk>/', ProductsUpdateDelete.as_view(), name='APIUDProduct'),

]

APIFirstProject/urls.py:

urlpatterns = [
    path('', include('AppAPI.urls'))
    path('api/', include('AppAPI.urls')),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]


http://127.0.0.1:8000/api/APIProduct/