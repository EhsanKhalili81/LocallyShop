from django.urls import path
from . import views


urlpatterns=[

    path('Cart/',views.Cart,name='Cart'),
    path('AddtoCart/<int:proid>/',views.addtocart,name='AddtoCart'),
    path('RemovePr/<int:proid>/',views.rmproduct,name='RemovePr'),
]