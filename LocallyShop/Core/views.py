from django.shortcuts import render
from .models import Category

# Create your views here.

def Home(request):
    ct=Category.objects.all()
    return render(request,'index.html',{'ct':ct})

def AcLogin(request):
    return render(request,'Login.html')

def AcRegister(request):
    return render(request,'Register.html')