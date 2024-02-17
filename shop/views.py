from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage
# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prodtt=None
    if c_slug != None:
        c_page= get_object_or_404(Category,slug=c_slug)
        prodtt=products.objects.filter(category=c_page,available=True)
    else:
        prodtt = products.objects.all().filter(available=True)
        paginator=Paginator(prodtt,2)
        try:
            page=int(request.GET.get('page'))
        except:
            page=1
        try:
            productts=paginator.page(page)
        except(InvalidPage,EmptyPage):
            productts=paginator.page(paginator.num_pages)

    cat=Category.objects.all()
    return render(request,'index.html',{'prod':productts,'cat':cat})
def home1(request,c_slug,product_slug):
    try:
        obj=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,"item.html",{'pr':obj})

def searching(request):
    query=None
    prod=None
    if "q" in request.GET:
        query=request.GET.get("q")
        prod=products.objects.all().filter(Q(name__contains=query)| Q(desc__contains=query))
    return render(request,"search.html",{"qr":query,"pr":prod})



