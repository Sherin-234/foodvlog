from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from ecommerceproject import settings
from . import views

urlpatterns = [
    path('cart/add/<int:product_id>/',views.addcart,name='addcart'),
    path('cart/cartDetails/',views.cartDetails,name='cartDetails'),
    path('cart/delete/<int:product_id>',views.delete,name='delete'),
]