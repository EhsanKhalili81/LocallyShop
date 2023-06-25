from django.shortcuts import render,redirect
from .models import Order,Basket
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
            c=basket.count + 1
            p=product.Price*c
            bs=Basket(id=basket.id,orderid=order1,productid=product,count=c,price=p)
        else:
            p=product.Price*c
            bs=Basket(orderid=order1,productid=product,count=1,price=p)    
        bs.save()
    else:
        messages.warning(request,'لطفا اول به حساب کاربری خود وارد شوید')
    # return render(request,'ProductDetail.html',{'pr':product})
   # t = request.META.get('HTTP_REFERER')
    return redirect('Cart')


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
    return render(request,'FinalOrder.html',{'userinfo':userinfo,'order':order})

def SubmitOrder(request):
    order=Order.objects.get(user=request.user,orderstatus=0)
    ordercomplete=Order(id=order.id,orderstatus=1,user=request.user,sumprice=order.sumprice)
    ordercomplete.save()
    if ordercomplete:
        messages.success(request,'ثبت سفارش با موفقیت انجام شد')
    else:
        messages.warning(request,'ثبت سفارش انجام نشد')
    return redirect('Home')