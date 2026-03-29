from django.urls import path

from .views import (
    CategoriesListCreate,
    CategoriesUpdateDelete,
    ProductsListCreate,
    ProductsUpdateDelete,
)

urlpatterns = [
    path('APICategory/', CategoriesListCreate.as_view(), name='APILCCategory'),
    path('APICategory/<int:pk>/', CategoriesUpdateDelete.as_view(), name='APIUDCategory'),
    path('APIProduct/', ProductsListCreate.as_view(), name='APILCProduct'),
    path('APIProduct/<int:pk>/', ProductsUpdateDelete.as_view(), name='APIUDProduct'),
]