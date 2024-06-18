from django.db import models
from .common import TimeStampedUUIDModel
from uuid import uuid4
from studio.models.section import Section


class Article(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE,related_name='articles', null=True)
    article_name = models.CharField(max_length=255,blank=True, unique=True)
    article_url = models.FileField(upload_to='media/')
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.article_name

    class Meta:
        ordering = ['order']