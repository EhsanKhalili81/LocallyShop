from django.shortcuts import render
from .models import Category
from Admin.models import Slider,Card
from Seller.models import Product

# Create your views here.

def Home(request):
    slider=Slider.objects.all()
    ct=Category.objects.all()
    card=Card.objects.all()
    return render(request,'index.html',{'slider':slider,'ct':ct,'card':card})

def AcLogin(request):
    return render(request,'Login.html')

def AcRegister(request):
    return render(request,'Register.html')

# def Products(request):
#     pr=Product.objects.all()
#     return render(request,'Product.html',{'pr':pr})

def ProductDetail(request,proid):
    pr=Product.objects.get(pk=proid)
    return render(request,'ProductDetail.html',{'pr':pr})

def Showproduct(request,ctid):
    pr=Product.objects.filter(category=ctid)
    return render(request,'Product.html',{'pr':pr})