from django.shortcuts import render,redirect

# Create your views here.
from .models import Product
from .models import CustomUSer, Cart, Order,OrderItem
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        
        if username and password:
            user = CustomUSer.objects.create_user(username=username,password=password, first_name=first_name)
            login(request, user)
            return redirect('home')
        return render(request, 'register.html', {'error': 'Invalid username or password.'})
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_to_cart(request, pk):
    user= request.user 
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product = Product.objects.get(id=pk) 
        quantity = request.POST.get('quantity')
          
        cart_item = Cart.objects.filter(user=user, product=product).first()
        if cart_item:
            cart_item.quantity += int(quantity)
            cart_item.save()
            return redirect('home')
        else:
            cart = Cart.objects.create(user=user, product=product, quantity=quantity)
            cart.save()
            return redirect('cart_detail')
        
    return render(request, 'shop-single-product-2.html', {'product':product})

def remove_cart(request, pk):
    cart_item = Cart.objects.filter(id=pk, user=request.user).first() 
    if cart_item:
        cart_item.delete() 
        return redirect('cart_detail')
    
    