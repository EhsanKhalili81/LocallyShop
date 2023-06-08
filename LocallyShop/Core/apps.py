from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Core'



def some_model_object(request):
    from .models import Category
    return {'my_object': Category.objects.all()}
