from django.shortcuts import render
from app.models import Product
# Create your views here.

def home(request):
    products = Product.objects.all().order_by('-id')
    return render(request, "index.html", {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'shop-single-product-2.html', {'product':product})

def contact(request):
    return render(request, 'contact.html')


def products(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'shop-list.html', {'products':products})