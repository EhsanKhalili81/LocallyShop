from django.shortcuts import render
from .models import Category
from Admin.models import Slider

# Create your views here.

def Home(request):
    slider=Slider.objects.all()
    return render(request,'index.html',{'slider':slider})

def AcLogin(request):
    return render(request,'Login.html')

def AcRegister(request):
    return render(request,'Register.html')