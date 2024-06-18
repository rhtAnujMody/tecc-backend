from django.db import models
from .common import TimeStampedUUIDModel
from uuid import uuid4
from studio.models.section import Section


class Video(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE,related_name='videos', null=True)
    video_name = models.CharField(max_length=255,blank=True, unique=True)
    video_url = models.FileField(upload_to='media/')
    order = models.PositiveIntegerField(default=0)
    duration = models.DurationField(null=True, blank=True)   # New duration field
    
    def __str__(self) -> str:
        return self.video_name
    
    class Meta:
        ordering = ['order']
