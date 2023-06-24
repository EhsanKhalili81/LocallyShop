from django.urls import path
from . import views


urlpatterns=[

    path('Homeadmin/',views.Homeadmin,name='Homeadmin'),
    path('User/<int:typeuser>/',views.Userinfo,name='User'),
    path('RemoveUser/<int:iduser>/',views.rmuser,name='RemoveUser'),
    path('EditUser/',views.EditUser,name='EditUser'),
]