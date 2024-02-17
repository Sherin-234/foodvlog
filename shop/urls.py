from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from ecommerceproject import settings
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.home1,name='prod_mod'),
    path('search',views.searching,name='search'),

]


