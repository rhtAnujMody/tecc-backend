from django.db import models
from studio.configs.constants import Constants
from uuid import uuid4


class Category(models.Model):
    CATEGORY_CHOICES = [
        (Constants.BEGINNER, Constants.BEGINNER),
        (Constants.INTERMEDIATE, Constants.INTERMEDIATE),
        (Constants.ADVANCED, Constants.ADVANCED),
        (Constants.PROFESSIONAL, Constants.PROFESSIONAL),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False) 
    name = models.CharField(max_length=255,choices=CATEGORY_CHOICES,unique=True)
    
    def __str__(self) -> str:
        return self.name