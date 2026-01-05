from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', views.remove_cart, name='remove_cart'),
    path('logout/', views.logout_view, name='logout'),
]