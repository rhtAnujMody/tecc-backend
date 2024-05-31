from django.db import models
from studio.models import Lesson
from .common import TimeStampedUUIDModel
from uuid import uuid4


class Quiz(TimeStampedUUIDModel):
    choices=[
        ('radio', 'Radio'),
        ('checkbox', 'Checkbox'),
        ('input', 'Input'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False,blank=True) 
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    question  = models.CharField(max_length=255)
    quiz_type = models.CharField(max_length=20,choices=choices)
    option = models.JSONField(blank=True,null=True)
    answer = models.JSONField()
    marks = models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.question
