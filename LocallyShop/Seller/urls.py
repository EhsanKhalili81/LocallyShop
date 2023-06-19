from django.urls import path
from . import views


urlpatterns=[

    path('SellerRequest/',views.SellerRequest,name='SellerRequest'),
]