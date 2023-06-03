from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def RegisterUser(request):
    Userinfo=User.objects.all()
    User_name=[]
    is_true=False
    if Userinfo != None:
        for i in Userinfo:
            User_name.append(i.username)
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if username not in User_name:
            User_Register=User.objects.create_user(password=password,username=username,email=email)
            User_Register.save()
            messages.success(request,'ثبت نام با موفقیت انجام شد')
            return redirect ('AcLogin')  
        else:
            messages.error(request,'ثبت نام متاسفانه انجام نشد نام کاربری تکراری است')
            return redirect ('AcRegister')   
           
        

def LoginUser(request):
    if request.method == 'POST':
        Username=request.POST['username']
        Password=request.POST['password']
        Userinfo=authenticate(request,username=Username,password=Password)
        if Userinfo is not None:
            messages.success(request,'ورود با موفقیت انجام شد ')
            login(request,Userinfo)
            return redirect ('Home') 
        else:
            messages.warning(request,'رمز ورود یا نام کاربری اشتباه است ')
            return redirect('AcLogin')

def LogoutUser(request):
        messages.info(request,'شما از حساب کاربری خود خارج شدید')
        logout(request) 
        return redirect('Home')