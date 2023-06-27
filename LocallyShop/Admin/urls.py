from django.urls import path
from . import views


urlpatterns=[

    path('Home/',views.Homeadmin,name='admin1/Home'),
    path('User/<int:typeuser>/',views.Userinfo,name='User'),
    path('RemoveUser/<int:iduser>/',views.rmuser,name='RemoveUser'),
    path('EditUser/<int:iduser>/',views.EditUser,name='EditUser'),
    path('AddUser/',views.AddUser,name='AddUser'),
    path('Register/',views.RegisterUser,name='Register'),
    path('Products/',views.products,name='Product'),
    path('RemoveProduct/<int:idpr>/',views.rmproduct,name='RemoveProduct'),
    path('AddProduct/',views.Addpr,name='AddProduct'),
    path('AddPt/',views.addproducts,name='AddPt'),
    path('EditProduct/<int:idpr>/',views.editpr,name='EditProduct'),
    path('EditPt/<int:idpr>/',views.editproduct,name='EditPt'),
]