from django.shortcuts import render
from .models import Order,Basket
from Seller.models import Product 

# Create your views here.
def Cart(request):
    return render(request,'ShoppingCart.html')


def addtocart(request,proid):
    order=Order.objects.filter(user=request.user,orderstatus=0)
    if order:
        order1=Order.objects.get(user=request.user,orderstatus=0)
    else:
        order_completed=Order(user=request.user)
        order_completed.save()
        order1=Order.objects.get(user=request.user,orderstatus=0)
    product=Product.objects.get(pk=proid)
    bs=Basket(orderid=order1,productid=product,count=1,price=product.Price)
    bs.save()
    return render(request,'ShoppingCart.html')