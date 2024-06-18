from django.db import models
from studio.models import Category,Profile
from .common import TimeStampedUUIDModel
from uuid import uuid4


class Course(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='courses')
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    thumbnail = models.FileField(upload_to='images/',default='images/course_thumbnail.jpg')
    profile = models.ManyToManyField(Profile,related_name='courses',null=True,blank=True) 
    credit = models.IntegerField(default=0, unique=False)
    is_mandatory = models.BooleanField(default=False,blank=False)
    
    def __str__(self) -> str:
        return self.title
