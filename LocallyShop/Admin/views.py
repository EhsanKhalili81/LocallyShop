from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Account.models import Userinformation
from django.contrib import messages
# Create your views here.
def Homeadmin(request):
    return render(request,'Admin/Home.html')

def Userinfo(request,typeuser):
    user=[]
    if typeuser == 3:
        user1=User.objects.filter(is_staff=True).values()
        messages.success(request,'ادمین ها')
    elif typeuser == 2:
        user0=Userinformation.objects.filter(is_seller=True).values()
        for i in user0:
            user1=User.objects.get(id=i['user_id'])
            user.append(user1)
        user1=user
        messages.success(request,'فروشندگان')
    else:
        user0=Userinformation.objects.filter(is_seller=False).values()
        for i in user0:
            user1=User.objects.get(is_staff=False,id=i['user_id']) 
            user.append(user1)
        user1=user
        messages.success(request,'کاربران عادی')       
    return render(request,'Admin/User.html',{'userinfo':user1})

def rmuser(request,iduser):
    user_deleted=User.objects.get(pk=iduser)
    user_deleted.delete()
    messages.success(request,'حذف با موفقیت انجام شد') 
    return redirect('Homeadmin')

def EditUser(request):
    return render(request,'Admin/EditUser.html')