from django.urls import path
from . import views


urlpatterns=[

    path('Home/',views.SellerHome,name='Seller/Home'),
]