from django.shortcuts import render

# Create your views here.

def SellerHome(request):
    return render(request,'Seller/Home.html')
