from django.urls import path
from . import views


urlpatterns=[

    path('Home/',views.Home,name='Home'),
    path('Login/',views.AcLogin,name='AcLogin'),
    path('Register/',views.AcRegister,name='AcRegister'),
    path('Products/<int:ctid>/',views.Showproduct,name='Products'),
    path('ProductDetail/<int:proid>/',views.ProductDetail,name='ProductDetail'),
    path('CheapProducts/',views.cheap,name='CheapProducts'),
    path('ExpensiveProducts/',views.Expensive,name='ExpensiveProducts'),
    path('NewProducts/',views.New,name='NewProducts'),
    path('AboutUs/',views.AboutUs,name='AboutUs'),
]