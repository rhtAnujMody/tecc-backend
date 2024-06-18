from .common import TimeStampedUUIDModel
from django.db import models
from .users import User
from django.core.exceptions import ValidationError
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
            ]    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username