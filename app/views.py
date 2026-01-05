from django.shortcuts import render
from app.models import Product, Category
from user.models import Cart
# Create your views here.

def home(request):
    products = Product.objects.all().order_by('-id')
    return render(request, "index.html", {'products': products})

def cart_detail(request):
    user =request.user
    items = Cart.objects.filter(user=user)
    
    all_total = 0
    for item in items:
        all_total+= item.total_price
    return render(request, 'shop-cart.html', {'items':items, 'all_total':all_total})
    
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    images = product.images.all()
    return render(request, 'shop-single-product-2.html', {'product':product, 'images':images})

def contact(request):
    return render(request, 'contact.html')


def products(request):
    cat_id = request.GET.get('category')
    if cat_id:
        products = Product.objects.filter(category_id=cat_id).order_by('-id')
    else:
        products = Product.objects.all().order_by('-id')
        
    categories = Category.objects.all()
    
    return render(request, 'shop-list.html', {'products':products, 'categories':categories})