from django.urls import path
from . import views


urlpatterns=[

    path('Cart/',views.Cart,name='Cart'),
]