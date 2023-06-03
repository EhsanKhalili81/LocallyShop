from django.urls import path
from . import views


urlpatterns=[

    path('RegisterUser/',views.RegisterUser,name='RegisterUser'),
    path('LoginUser/',views.LoginUser,name='LoginUser'),
    path('LogoutUser/',views.LogoutUser,name='LogoutUser'),
]