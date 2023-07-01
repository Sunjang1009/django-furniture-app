from django.db import models
from decimal import Decimal

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    bio = models.CharField(max_length=500)
    verified_brand = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('100.00'))
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name

    def get_price(self):
        return f"${self.price:,.2f}"

class Shoppinglist(models.Model):
    name = models.CharField(max_length=150)
    products = models.ManyToManyField(Product)
    def __str__(self):
        return self.name



