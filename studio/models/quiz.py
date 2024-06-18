from django.db import models
from studio.models.section import Section
from .common import TimeStampedUUIDModel
from uuid import uuid4


class Quiz(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False,blank=True, unique=True) 
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='quizs', null=True)
    quiz_name = models.CharField(max_length=255,blank=True, unique=True)
    quiz_schema = models.JSONField()
    is_mandatory = models.BooleanField(default=False,blank=False)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.quiz_name
    
    class Meta:
        ordering = ['order']
