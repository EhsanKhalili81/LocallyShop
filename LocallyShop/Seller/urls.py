from django.urls import path
from . import views


urlpatterns=[

    path('Home/',views.SellerHome,name='Seller/Home'),
    path('Products/',views.Products,name='Seller/Products'),
    path('Rmpr/<int:idpr>/',views.Rmpr,name='Rmpr'),
    path('AddProduct/',views.AddProduct,name='Seller/AddProduct'),
    path('addpr/',views.addpr,name='Seller/addpr'),
    path('Editpr/<int:idpr>/',views.Editpr,name='Seller/Editpr'),
    path('editproduct/<int:idpr>/',views.editproduct,name='Seller/editproduct'),
    path('SoldProducts/',views.SoldProducts,name='Seller/SoldProducts'),
    path('comments/',views.comments,name='Seller/comments'),
]