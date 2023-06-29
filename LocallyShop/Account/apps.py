from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Account'


def is_seller(request):
    user=0
    from .models import Userinformation
    if request.user.id:
        user=Userinformation.objects.get(user=request.user)
    return {'userinfo':user }
