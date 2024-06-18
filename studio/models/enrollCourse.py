from django.db import models
from studio.models import Course,Profile
from django.core.validators import MaxValueValidator, MinValueValidator
from .common import TimeStampedUUIDModel
from uuid import uuid4


class EnrollCourse(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)  
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    course_progress = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)],blank=True,null=True)
    is_enrolled = models.BooleanField(default=False,blank=True)
    is_CourseCompleted = models.BooleanField(default=False,blank=True)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    course_completion_date = models.DateTimeField(null=True,blank=True)
    total_chapter = models.IntegerField(default=0,null=True)
    completed_chapter = models.IntegerField(default=0,null=True)

    class Meta:
        unique_together = ('profile','course_id')

    def __str__(self) -> str:
        return str(self.profile)