from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('products/detail/<int:pk>', views.product_detail, name='product_detail'),
]