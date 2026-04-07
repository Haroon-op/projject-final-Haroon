from django.urls import path
from .views import ProductAPI


urlpatterns = [
    path('products/', ProductAPI.as_view()),
    
    
]

from django.urls import path
from .views import ProductAPI, ProductGetAPI

urlpatterns = [
    path('products/', ProductAPI.as_view(), name='product-create'),   
    path('products/get/', ProductGetAPI.as_view(), name='product-get')  
]
