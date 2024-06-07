from django.db import models
from studio.models import Video
from .common import TimeStampedUUIDModel
from uuid import uuid4


class Article(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE,related_name='articles')
    article_name = models.CharField(max_length=255,blank=True)
    article_url = models.FileField(upload_to='media/')
    
    def __str__(self) -> str:
        return self.article_name
