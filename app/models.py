from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name 
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    desc = models.TextField() 
    quantity = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class ProductImages(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        return self.product.name
    

class ProductExtraInfo(models.Model):
        size = models.PositiveIntegerField(null=True, blank=True)
        color = models.CharField(max_length=250, null=True, blank=True)
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='extra_infos')
        
        def __str__(self):
            return self.product.name