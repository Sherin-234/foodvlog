from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from ecommerceproject import settings
from . import views

urlpatterns = [
    path('account/register',views.register,name='register'),
    path('account/login',views.login,name='login'),

]