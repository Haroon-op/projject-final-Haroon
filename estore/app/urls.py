from django.urls import path
from .views import ProductAPI


urlpatterns = [
    path('products/', ProductAPI.as_view()),
    
]