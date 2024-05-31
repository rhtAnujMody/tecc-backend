from django.db import models
from studio.models import Category,Profile
from .common import TimeStampedUUIDModel
from uuid import uuid4


class Jobs(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)  
    job_title = models.CharField(max_length=255)
    thumbnail = models.FileField(upload_to='images/',default='images/jobs_thumbnail.jpg')
    Location = models.CharField(max_length=255)
    Service_type = models.CharField(max_length=255)
    Industry = models.CharField(max_length=255)
    Experience = models.CharField(max_length=255)
    Required_skills = models.CharField(max_length=255)
    Compensation = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.job_title + self.Location
