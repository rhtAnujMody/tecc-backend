from django.db import models
from studio.models import Profile,Jobs
from .common import TimeStampedUUIDModel
from uuid import uuid4


class AppliedJobs(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)  
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    is_applied = models.BooleanField(default=False)
    applied_date = models.DateTimeField(auto_now_add=True)

    class meta:
        unique_together=('profile','job')
    
    def __str__(self) -> str:
        return str(self.profile) + str(self.job)
