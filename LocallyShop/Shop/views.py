from django.shortcuts import render,redirect
from .models import Order,Basket,Comments
from Seller.models import Product 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from Account.models import Userinformation
from django.contrib import messages
# Create your views here.
def Cart(request):
    if request.user.id:
        order=Order.objects.get(user=request.user,orderstatus=0)
        bs=Basket.objects.filter(orderid=order).values()
        pr=[]
        sumprice1=0
        for i in list(bs):
            pr.append(Product.objects.get(pk=i['productid_id']))
            sumprice1 += i['price']
        or1=Order(id=order.id,sumprice=sumprice1,user=request.user)
        or1.save()
        if or1 :
            order=Order.objects.get(user=request.user,orderstatus=0)
    else:
        return redirect('Home')
    return render(request,'ShoppingCart.html',{'basket':bs,'pr':pr,'order':order})


def addtocart(request,proid):
    if request.user.id:
        c=1
        order=Order.objects.filter(user=request.user,orderstatus=0)
        if order:
            order1=Order.objects.get(user=request.user,orderstatus=0)
        else:
            order_completed=Order(user=request.user)
            order_completed.save()
            order1=Order.objects.get(user=request.user,orderstatus=0)
        product=Product.objects.get(pk=proid)
        basket=Basket.objects.filter(orderid=order1,productid=product)
        if basket:
            basket=Basket.objects.get(orderid=order1,productid=product)
            if basket.countp+1 > product.Qty:
                messages.warning(request,"موجودی محصول کافی نیست .")
                return redirect('Home')
            else:
                c=basket.countp + 1
                p=product.Price*c
                bs=Basket(id=basket.id,orderid=order1,productid=product,countp=c,price=p)
        else:
            if  product.Qty == 0:
                messages.warning(request,"موجودی محصول کافی نیست .")
                return redirect('Home')
            else:
                p=product.Price*c
                bs=Basket(orderid=order1,productid=product,countp=1,price=p)  
        bs.save()
    else:
        messages.warning(request,'لطفا اول به حساب کاربری خود وارد شوید')
        return redirect('Home')   
    return redirect(request.META.get('HTTP_REFERER'))


def rmproduct(request,proid):
    order=Order.objects.get(user=request.user,orderstatus=0)
    bs=Basket.objects.get(orderid=order,productid=proid)
    bs.delete()
    return redirect('Cart')

def Showorders(request):
    order=Order.objects.filter(user=request.user)
    pr=Product.objects.all()
    bs=Basket.objects.all()
    return render(request,'OrderDetails.html',{'order':order,'bs':bs,'pr':pr})


def FinalOrder(request):
    user=User.objects.get(pk=request.user.id)
    userinfo=Userinformation.objects.get(user=user)
    order=Order.objects.get(user=user,orderstatus=0)
    if userinfo.address is None or userinfo.kodeposti is None :
        messages.success(request,'لطفا کد پستی یا آدرس خود را ثبت کنید')
        return redirect('Home')
    else:
        return render(request,'FinalOrder.html',{'userinfo':userinfo,'order':order})

def SubmitOrder(request):
    a=0
    order=Order.objects.get(user=request.user,orderstatus=0)
    ordercomplete=Order(id=order.id,orderstatus=1,user=request.user,sumprice=order.sumprice)
    ordercomplete.save()
    if ordercomplete:
        bs=Basket.objects.filter(orderid=order)
        for i in bs:
            a=i.productid.Qty-i.countp
            predit=Product(pk=i.productid.pk,User=i.productid.User,Title=i.productid.Title,Description=i.productid.Description,category=i.productid.category,Qty=a,Price=i.productid.Price,Image=i.productid.Image,Size=i.productid.Size)
            predit.save()
        messages.success(request,'ثبت سفارش با موفقیت انجام شد')
    else:
        messages.warning(request,'ثبت سفارش انجام نشد')
    return redirect('Home')

def AddComment(request,proid):
    pr=Product.objects.get(pk=proid)
    if request.method == 'POST':
         comment = request.POST['comment']
         if comment == "":
             pass
         else:
            if request.user.id:
                cm=Comments(user=request.user,product=pr,comment=comment)
                cm.save()
            else:
                cm=Comments(user=None,product=pr,comment=comment)
                cm.save()
    return redirect(request.META.get('HTTP_REFERER'))
