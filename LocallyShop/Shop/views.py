from django.shortcuts import render,redirect
from .models import Order,Basket
from Seller.models import Product 
from django.http import HttpResponseRedirect

# Create your views here.
def Cart(request):
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
    return render(request,'ShoppingCart.html',{'basket':bs,'pr':pr,'order':order})


def addtocart(request,proid):
    c=1
    order=Order.objects.filter(user=request.user,orderstatus=0)
    if order:
        order1=Order.objects.get(user=request.user,orderstatus=0)
    else:
        order_completed=Order(user=request.user)
        order_completed.save()
        order1=Order.objects.get(user=request.user,orderstatus=0)
    product=Product.objects.get(pk=proid)
    basket=Basket.objects.filter(productid=product)
    if basket:
        basket=Basket.objects.get(productid=product)
        c=basket.count + 1
        p=product.Price*c
        bs=Basket(id=basket.id,orderid=order1,productid=product,count=c,price=p)
    else:
        p=product.Price*c
        bs=Basket(orderid=order1,productid=product,count=1,price=p)    
    bs.save()
    # t = request.META.get('HTTP_REFERER')
    return render(request,'ProductDetail.html',{'pr':product})
    # return redirect('ProductDetail',pr=product)


def rmproduct(request,proid):
    order=Order.objects.get(user=request.user,orderstatus=0)
    bs=Basket.objects.get(orderid=order,productid=proid)
    bs.delete()
    return redirect('Cart')