from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.hashers import check_password

# # Create your models here.
# class User(AbstractBaseUser):
#     Username=models.CharField(max_length=255,unique=True)
#     Email=models.EmailField(max_length=255)
#     is_admin=models.BooleanField(default=False)


#     USERNAME_FIELD = 'Username'
#     REQUIRED_FIELDS = ['Email']

#     def authenticate(request,username=None, password=None):
#         try:
#         # Get the corresponding user.
#             user = User.objects.get(Username=username)
#         #  If password, matches just return the user. Otherwise, return None.
#             if check_password(password, user.password):
#                 return user
#             return None
#         except User.DoesNotExist:
#         # No user was found.
#             return None

