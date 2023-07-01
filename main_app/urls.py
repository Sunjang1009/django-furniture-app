from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('brands/',views.BrandList.as_view(), name="brand_list"),
    path('brands/new/',views.BrandCreate.as_view(), name="brand_create"),
    path('brands/<int:pk>/', views.BrandDetail.as_view(), name="brand_detail"),
    path('brands/<int:pk>/update/', views.BrandUpdate.as_view(), name="brand_update"),
    path('brands/<int:pk>/delete/', views.BrandDelete.as_view(), name="brand_delete"),
    path('brands/<int:pk>/products/new/', views.ProductCreate.as_view(), name="product_create"),
    path('shoppinglists/<int:pk>/products/<int:product_pk>/', views.ShoppinglistProductAssoc.as_view(), name="shoppinglist_product_assoc"),
]











