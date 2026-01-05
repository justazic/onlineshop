from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('products/detail/<int:pk>', views.product_detail, name='product_detail'),
]