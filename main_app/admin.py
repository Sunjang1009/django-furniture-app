from django.contrib import admin
from .models import Brand, Product, Shoppinglist

# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Shoppinglist)


