from django.urls import path
from . import views


urlpatterns=[

    path('Home/',views.Homeadmin,name='admin1/Home'),
    path('User/<int:typeuser>/',views.Userinfo,name='User'),
    path('RemoveUser/<int:iduser>/',views.rmuser,name='RemoveUser'),
    path('EditUser/<int:iduser>/',views.EditUser,name='EditUser'),
    path('AddUser/',views.AddUser,name='AddUser'),
    path('Register/',views.RegisterUser,name='Register'),
]