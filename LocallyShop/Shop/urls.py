from django.urls import path
from . import views


urlpatterns=[

    path('Cart/',views.Cart,name='Cart'),
    path('AddtoCart/<int:proid>/',views.addtocart,name='AddtoCart'),
    path('RemovePr/<int:proid>/',views.rmproduct,name='RemovePr'),
    path('Showorders/',views.Showorders,name='Showorders'),
    path('FinalOrder/',views.FinalOrder,name='FinalOrder'),
    path('SubmitOrder/',views.SubmitOrder,name='SubmitOrder'),
    path('AddComment/<int:proid>/',views.AddComment,name='AddComment'),
    path('Malyat/',views.Malyatamount,name='Malyat'),
    path('updateml/<int:mlid>/',views.updateml,name='updateml'),
]