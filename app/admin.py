from django.contrib import admin

# Register your models here.

from .models import Category,Product, ProductImages,ProductExtraInfo 

admin.site.register([Product,ProductImages,ProductExtraInfo,Category])