from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Account.models import Userinformation
from Shop.models import Order
from django.contrib import messages
from django.db.models import Q
from Seller.models import Product
from Core.models import Category
# Create your views here.
def Homeadmin(request):
    if request.user.is_staff :
        gardesh=0
        seller=Userinformation.objects.filter(is_seller=True).count()
        user=User.objects.all().count()
        order=Order.objects.filter(Q(orderstatus=1) | Q(orderstatus=2)).count()
        orderprice=Order.objects.filter(Q(orderstatus=1) | Q(orderstatus=2)).values()
        for i in orderprice:
            gardesh+=int(i['sumprice'])
        return render(request,'Admin/Home.html',{'seller':seller,'user':user,'order':order,'gardesh':gardesh})
    else :
        messages.warning(request,'شما دسترسی ادمین ندارید .') 
        return redirect('Home')

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
            if User.objects.filter(is_staff=False,pk=i['user_id']):
                user1=User.objects.get(is_staff=False,pk=i['user_id'])
                user.append(user1)
        user1=user
        messages.success(request,'کاربران عادی')       
    return render(request,'Admin/User.html',{'userinfo':user1})

def rmuser(request,iduser):
    user_deleted=User.objects.get(pk=iduser)
    user_deleted.delete()
    messages.success(request,'حذف با موفقیت انجام شد') 
    return redirect('admin1/Home')

def EditUser(request,iduser):
    admin=False
    seller=False
    userinfo=User.objects.get(pk=iduser)
    userinfocompleted=Userinformation.objects.get(user=userinfo)
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        lname=request.POST['lname']
        typeuser=int(request.POST['usertype'])
        if typeuser == 1 :
            seller=False
            admin=False
        elif typeuser == 2 :
            seller=True
            admin=False
        elif typeuser == 3 :
            seller=False
            admin=True 
        User_Register=User(pk=userinfo.id,is_staff=admin,username=userinfo.username,email=email,first_name=name,last_name=lname)
        User_Register.save()
        userinformation=Userinformation(user=User_Register,is_seller=seller,tel=request.POST['tel'],address=request.POST['address'],kodeposti=request.POST['kodeposti'])
        userinformation.save()
        if User_Register and userinformation:
            messages.success(request,'ویرایش  با موفقیت انجام شد')
            return redirect ('admin1/Home')  
        else:
            messages.error(request,'متاسفانه عملیت ویرایش انجام نشد.')
            return redirect ('admin1/Home')  
    return render(request,'Admin/EditUser.html',{'user':userinfo,'userinfo':userinfocompleted})

def AddUser(request):
    return render(request,'Admin/AddUser.html')

def RegisterUser(request):
    admin=False
    seller=False
    Userinfo=User.objects.all()
    User_name=[]
    if Userinfo != None:
        for i in Userinfo:
            User_name.append(i.username)
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        name=request.POST['name']
        lname=request.POST['lname']
        typeuser=int(request.POST['usertype'])
        if typeuser == 1 :
            seller=False
            admin=False
        elif typeuser == 2 :
            seller=True
            admin=False
        elif typeuser == 3 :
            seller=False
            admin=True     
        if username not in User_name:
            User_Register=User.objects.create_user(password=password,username=username,is_staff=admin,email=email,first_name=name,last_name=lname)
            User_Register.save()
            userinformation=Userinformation(user=User_Register,tel=request.POST['tel'],is_seller=seller,address=request.POST['address'],kodeposti=request.POST['kodeposti'])
            userinformation.save()
            messages.success(request,'ثبت نام با موفقیت انجام شد')
            return redirect ('admin1/Home')  
        else:
            messages.error(request,'ثبت نام متاسفانه انجام نشد نام کاربری تکراری است')
            return redirect ('admin1/Home')  

def products(request):
    pr=Product.objects.all()
    messages.success(request,'محصولات')
    return render(request,'Admin/Products.html',{'pr':pr})

def rmproduct(request,idpr):
    pr_deleted=Product.objects.get(pk=idpr)
    pr_deleted.delete()
    messages.success(request,'حذف با موفقیت انجام شد') 
    return redirect('admin1/Home')

def Addpr(request):
    seller=[]
    user0=Userinformation.objects.filter(is_seller=True).values()
    for i in user0:
        user1=User.objects.get(id=i['user_id'])
        seller.append(user1)
    return render(request,'Admin/AddProducts.html',{'seller':seller})

def addproducts(request):
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        image =request.FILES['image']
        user=request.POST['seller']
        seller=User.objects.get(pk=user)
        cty=request.POST['category']
        ct=Category.objects.get(pk=cty)
        price=request.POST['price']
        size=request.POST['size']
        qty=request.POST['qty']
        qtysell=request.POST['qtysell']
        pr=Product(User=seller,Title=name,Description=description,category=ct,Price=price,Size=size,Qty=qty,Qtysell=qtysell,Image=image)
        pr.save()
    if pr :
        messages.success(request,'محصول با موفقیت اضافه شد .')
    else :
        messages.warning(request,'متاسفانه محصول اضافه نشد .')       
    return redirect('admin1/Home')
def editpr(request,idpr):
    pr=Product.objects.get(pk=idpr)
    return render(request,'Admin/EditProducts.html',{'pr':pr})

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
        qtysell=requset.POST['qtysell']
        pr=Product(pk=idpr,User=pro.User,Title=name,Description=description,category=ct,Price=price,Size=size,Qty=qty,Qtysell=qtysell,Image=image)
        pr.save()
    if pr :
        messages.success(requset,'محصول با موفقیت ویرایش شد .')
    else :
        messages.warning(requset,'متاسفانه محصول ویرایش نشد .')
    return redirect('admin1/Home')
