from django.urls import path

from .views import (
    CategoriesListCreate,
    CategoriesUpdateDelete,
    home,
    ProductsListCreate,
    ProductsUpdateDelete,
)

urlpatterns = [
    path('', home, name='home'),
    path('APICategory/', CategoriesListCreate.as_view(), name='APILCCategory'),
    path('APICategory/<int:pk>/', CategoriesUpdateDelete.as_view(), name='APIUDCategory'),
    path('APIProduct/', ProductsListCreate.as_view(), name='APILCProduct'),
    path('APIProduct/<int:pk>/', ProductsUpdateDelete.as_view(), name='APIUDProduct'),
]