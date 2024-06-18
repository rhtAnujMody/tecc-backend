from django.db import models
from studio.configs.constants import Constants
from uuid import uuid4


class Category(models.Model):
    CATEGORY_CHOICES = [
        (Constants.HEALTHCARE, Constants.HEALTHCARE),
        (Constants.TECHNOLOGY, Constants.TECHNOLOGY),
        (Constants.FINANCE, Constants.FINANCE),
        (Constants.COMMUNICATION, Constants.COMMUNICATION),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False) 
    name = models.CharField(max_length=255,unique=True)
    description = models.CharField(max_length=255)
    thumbnail = models.FileField(upload_to='images/',default='images/category_thumbnail.jpg')

    USERNAME_FIELD = "name"
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"