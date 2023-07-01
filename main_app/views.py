from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Brand, Product, Shoppinglist


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shoppinglists"] = Shoppinglist.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class BrandList(TemplateView):
    template_name = "brand_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["brands"] = Brand.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:    
            context["brands"] = Brand.objects.all()
            context["header"] = "Trending Brands for Furniture"
        return context

class BrandCreate(CreateView):
    model = Brand
    fields = ["name", "image", "bio", "verified_brand"]
    template_name = "brand_create.html"
    def get_success_url(self):
        return reverse('brand_detail', kwargs={'pk':self.object.pk})

class BrandDetail(DetailView):
    model = Brand
    template_name = "brand_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shoppinglists"] = Shoppinglist.objects.all()
        return context

class BrandUpdate(UpdateView):
    model = Brand
    fields = ["name", "image", "bio", "verified_brand"]
    template_name = "brand_update.html"
    def get_success_url(self):
        return reverse('brand_detail', kwargs={'pk':self.object.pk})

class BrandDelete(DeleteView):
    model = Brand
    template_name = "brand_delete_confirmation.html"
    success_url = "/brands/"

class ProductCreate(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        color = request.POST.get("color")
        price = request.POST.get("price")
        brand = Brand.objects.get(pk=pk)
        Product.objects.create(name=name, color=color, price=price, brand=brand)
        return redirect('brand_detail', pk=pk)

class ShoppinglistProductAssoc(View):
    def get(self, request, pk, product_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Shoppinglist.objects.get(pk=pk).products.remove(product_pk)
        if assoc == "add":
            Shoppinglist.objects.get(pk=pk).products.add(product_pk)
        return redirect('home')

