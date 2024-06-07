from django.db import models
from studio.models import Lesson
from .common import TimeStampedUUIDModel
from uuid import uuid4


class Video(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE,related_name='videos')
    video_name = models.CharField(max_length=255,blank=True)
    video_url = models.FileField(upload_to='media/')
    #is_video_completed = models.BooleanField(default=False,blank=True)
    
    def __str__(self) -> str:
        return self.video_name
