from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from shop.models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# def cart(request):
#     return render(request,'cart.html')

def cart_idd(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def addcart(request,product_id):
    prodd=products.objects.get(id=product_id)
    try:
        ctt_id=cart_id.objects.get(c_id=cart_idd(request))
    except cart_id.DoesNotExist:
        ctt_id=cart_id.objects.create(c_id=cart_idd(request))
    try:
        c_items=Items.objects.get(prodt=prodd,cart=ctt_id,quantity=1)
        if(c_items.quantity < c_items.prodt.stock):
            c_items.quantity+=1
        c_items.save()
    except Items.DoesNotExist:
        c_items=Items.objects.create(prodt=prodd,cart=ctt_id,quantity=1)
        c_items.save()
    return redirect('cartDetails')

def cartDetails(request,total=0,count=0,ct_items=None):
    try:
        ctt_id=cart_id.objects.get(c_id=cart_idd(request))
        ct_items=Items.objects.filter(active=True,cart=ctt_id)
        for i in ct_items:
            total+=i.quantity * i.prodt.price
            count+=i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,"cart.html",{'ci':ct_items,'t':total,'c':count})

def delete(request,product_id):
    prod=get_object_or_404(products,id=product_id)
    ct=cart_id.objects.get(c_id=cart_idd(request))
    c_items=Items.objects.get(cart=ct,prodt=prod)
    c_items.delete()
    return render("cart/cartDetails")


