from django.shortcuts import render
from .models import Category
from Admin.models import Slider,Card
from Seller.models import Product
from Shop.models import Order,Comments
from django.utils import timezone

# Create your views here.

def Home(request):
    if request.user.id:
        order=Order.objects.filter(user=request.user,orderstatus=0)
        if order:
            pass
        else:
            ordercreate=Order(user=request.user,orderstatus=0,sumprice=0)
            ordercreate.save()
    slider=Slider.objects.all()
    card=Card.objects.all()
    return render(request,'index.html',{'slider':slider,'card':card})

def AcLogin(request):
    return render(request,'Login.html')

def AcRegister(request):
    return render(request,'Register.html')
# def Products(request):
#     pr=Product.objects.all()
#     return render(request,'Product.html',{'pr':pr})

def ProductDetail(request,proid):
    pr=Product.objects.get(pk=proid)
    cm=Comments.objects.filter(product=pr).order_by('-date_created')
    return render(request,'ProductDetail.html',{'pr':pr,'comments':cm})

def Showproduct(request,ctid):
    pr=Product.objects.filter(category=ctid)
    return render(request,'Product.html',{'pr':pr})

def cheap(request):
    Pr=Product.objects.all().order_by('Price')
    return render(request,'Product.html',{'pr':Pr})

def Expensive(request):
    Pr=Product.objects.all().order_by('-Price')
    return render(request,'Product.html',{'pr':Pr})

def New(request):
    Pr=Product.objects.all().order_by('-id')
    return render(request,'Product.html',{'pr':Pr})

def AboutUs(request):
    return render(request,'AboutUs.html')