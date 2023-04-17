from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):

    # Set Username 'None' in default
    username = None

    # Define field we want to extend in custom user model
    email = models.EmailField(max_length=254,unique=True)
    mobile = models.CharField(max_length=50,blank=True)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    forget_password_token  = models.CharField( max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    # Set Default feild for login and It must have the attribute "unique=True"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


