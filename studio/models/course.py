from django.db import models
from studio.models import Category,Profile
from .common import TimeStampedUUIDModel
from uuid import uuid4


class Course(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)  
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    thumbnail = models.FileField(upload_to='images/',default='images/course_thumbnail.jpg')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='courses')
    duration = models.CharField(max_length=100,null=True,blank=True)
    profile = models.ManyToManyField(Profile,related_name='courses',null=True,blank=True)
    is_enrolled = models.BooleanField(default=False,blank=True)
    instructor_name = models.CharField(max_length=255,blank=True)
    instructor_signature = models.FileField(upload_to='images/',default='images/signature.jpg',blank=True)  
    
    def __str__(self) -> str:
        return self.title
