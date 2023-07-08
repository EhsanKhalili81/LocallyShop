from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Product
from Shop.models import Order,Basket,Comments
from django.db.models import Q
from Core.models import Category
from Account.models import Userinformation
from django.contrib.auth.models import User
# Create your views here.

def SellerHome(request):
    user=Userinformation.objects.get(user=request.user)
    if user.is_seller:
        pro=0
        finallprice=0
        pr=Product.objects.filter(User=request.user).count()
        ord=Order.objects.filter(Q(orderstatus=1) | Q(orderstatus=2))
        for i in ord:
            bs=Basket.objects.filter(orderid=i)
            if bs:
                for x in bs:
                    if x.productid.User == request.user:
                        pro+=x.countp
                        finallprice +=(x.productid.Price*x.countp)
        return render(request,'Seller/Home.html',{'pr':pr,'prs':pro,'price':finallprice})
    else:
        messages.warning(request,'شما دسترسی فروشندگی ندارید .') 
        return redirect('Home')

def Products(request):
    pr=Product.objects.filter(User=request.user)
    messages.success(request,'محصولات')
    return render(request,'Seller/Products.html',{'pr':pr})

def Rmpr(request,idpr):
    pr=Product.objects.get(pk=idpr)
    pr.delete()
    messages.success(request,'محصول با موفقیت حذف شد .')
    return redirect('Seller/Home')

def AddProduct(request):
    return render(request,'Seller/AddProducts.html')

def addpr(request):
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        image =request.FILES['image']
        cty=request.POST['category']
        ct=Category.objects.get(pk=cty)
        price=request.POST['price']
        size=request.POST['size']
        qty=request.POST['qty']
        pr=Product(User=request.user,Title=name,Description=description,category=ct,Price=price,Size=size,Qty=qty,Image=image)
        pr.save()
    if pr :
        messages.success(request,'محصول با موفقیت اضافه شد .')
    else :
        messages.warning(request,'متاسفانه محصول اضافه نشد .')       
    return redirect('Seller/Home')

def Editpr(request,idpr):
    pr=Product.objects.get(pk=idpr)
    return render(request,'Seller/EditProduct.html',{'pr':pr})

def editproduct(requset,idpr):
    pro=Product.objects.get(pk=idpr)
    if requset.method=='POST':
        name=requset.POST['name']
        description=requset.POST['description']
        image =requset.FILES.get('image',pro.Image)
        cty=requset.POST['category']
        ct=Category.objects.get(pk=cty)
        price=requset.POST['price']
        size=requset.POST['size']
        qty=requset.POST['qty']
        pr=Product(pk=idpr,User=requset.user,Title=name,Description=description,category=ct,Price=price,Size=size,Qty=qty,Image=image)
        pr.save()
    if pr :
        messages.success(requset,'محصول با موفقیت ویرایش شد .')
    else :
        messages.warning(requset,'متاسفانه محصول ویرایش نشد .')
    return redirect('Seller/Home')

def SoldProducts(request):
    sold=[]
    ord=Order.objects.filter(Q(orderstatus=1) | Q(orderstatus=2))
    for x in ord:
        bs=Basket.objects.filter(orderid=x)
        for i in bs:
            if i.productid.User == request.user:
                sold.append(i)
    messages.success(request,'کالاهای فروخته شده')            
    return render(request,'Seller/SoldProducts.html',{'pr':sold})     

def comments(request):
    com=[]
    pr=Product.objects.filter(User=request.user)
    for i in pr:
        cm=Comments.objects.filter(product=i)
        com.append(cm)
    messages.success(request,'نظرات')           
    return render(request,'Seller/Comments.html',{'cm':com})   
