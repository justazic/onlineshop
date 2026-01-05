from django.db import models
from decimal import Decimal
# Create your models here.

from django.contrib.auth.models import User,AbstractUser
from app.models import Product

class CustomUSer(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    
    
    def __str__(self):
        return self.first_name
    
class Cart(models.Model):
    user = models.ForeignKey(CustomUSer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    total_price = models.PositiveBigIntegerField(default=0)
    
    def save(self, *args, **kwargs):
        price = self.product.discount_price or self.product.price
        total_price = price * Decimal(self.quantity)
        self.total_price = total_price
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.user.username}--{self.product.name}"
    
    
class Order(models.Model):
    user = models.ForeignKey(CustomUSer, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True, related_name='items')
    total_price = models.PositiveBigIntegerField(default=0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(default=0)
    quantity = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.order.user.username