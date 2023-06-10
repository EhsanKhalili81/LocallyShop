from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Shop'




def basketcounter(request):
    from Shop.models import Order,Basket
    bs=""
    if request.user.id:
        order=Order.objects.get(user=request.user,orderstatus=0)
        bs=Basket.objects.filter(orderid=order)
    return {'counter': len(bs)}
