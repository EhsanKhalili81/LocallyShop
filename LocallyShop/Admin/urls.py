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
    path('Slider/',views.Sliders,name='Slider'),
    path('EditSlider/<int:idsl>/',views.EditSlider,name='EditSlider'),
    path('EditedSlider/<int:idsl>/',views.Editsl,name='EditedSlider'),
    path('Card/',views.Cards,name='Card'),
    path('EditCard/<int:idcrd>/',views.EditCard,name='EditCard'),
    path('EditedCard/<int:idcrd>/',views.Editcrd,name='EditedCard'),
    path('SellerRQ/',views.SellerRQ,name='SellerRQ'),
    path('SRQAccept/<int:iduser>/',views.SRQAccept,name='SRQAccept'),
    path('SRQDeclined/<int:iduser>/',views.SRQDeclined,name='SRQDeclined'),
    path('OrderRecieve/',views.OrderRecieve,name='OrderRecieve'),
    path('Orders/',views.Orders,name='Orders'),
    path('SubmitOrder/<int:idorder>/',views.SubmitOrder,name='SubmitOrder'),
    path('Category/',views.Categories,name='Category'),
    path('Removect/<int:idct>/',views.Removect,name='Removect'),
    path('Addct/',views.Addct,name='Addct'),
    path('AddNewCt/',views.AddNewCt,name='AddNewCt'),
    path('Editct/<int:idct>/',views.Editct,name='Editct'),
    path('EditSelectedCt/<int:idct>/',views.EditSelectedCt,name='EditSelectedCt'),
    path('comments/',views.comments,name='comments'),
    path('RmComment/<int:cmid>/',views.RmComment,name='RmComment'),
    
]