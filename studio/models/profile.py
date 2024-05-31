from .common import TimeStampedUUIDModel
from django.db import models
from .users import User
from django.core.exceptions import ValidationError
from auditlog.registry import auditlog
from studio.configs import Constants


def validate_phone(value):
    if value and len(value) == 10:
        return value
    else:
        raise ValidationError("Please enter a valid 10 digit phone number.")
    

class Profile(TimeStampedUUIDModel):
    
    GENDER_CHOICES = [
        (Constants.MALE, Constants.MALE),
        (Constants.FEMALE, Constants.FEMALE),
        (Constants.OTHERS, Constants.OTHERS),
    ]
    ROLE_CHOICES = [
        (Constants.NURSE, Constants.NURSE),
        (Constants.ADMIN, Constants.ADMIN)
    ]
    
    class Meta:
        app_label = "studio"
        db_table = "profile"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['full_name',]),
            models.Index(fields=['phone',]),
            ]    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10,null=True, unique=True, validators=[validate_phone])
    country_code = models.CharField(max_length=5, default='+91')
    city = models.CharField(max_length=50)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    
    def __str__(self):
        return self.user.username