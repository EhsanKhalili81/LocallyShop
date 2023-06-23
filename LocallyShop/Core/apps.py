from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Core'



def category(request):
    from .models import Category
    return {'category': Category.objects.all()}

