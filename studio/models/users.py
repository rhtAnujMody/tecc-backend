from django.db import models
from django.core.exceptions import ValidationError
from auditlog.registry import auditlog
from studio.configs import Constants
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
import uuid


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = 'studio'
        db_table = 'user'
        
    pkid = models.BigAutoField(primary_key=True, editable=False)    
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=255, unique=False)
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    qualification = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True,unique=True)
    state = models.CharField(max_length=50,null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name","qualification","phone","state"]

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def get_short_name(self):
        return self.username
