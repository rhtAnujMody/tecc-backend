from django.db import models
from .course import Course
from studio.models import Profile,Lesson
from .common import TimeStampedUUIDModel
from uuid import uuid4


class LessonCompletion(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False) 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    video_completed = models.BooleanField(default=False)
    article_completed = models.BooleanField(default=False)
    quiz_completed = models.BooleanField(default=False)
    quiz_marks = models.FloatField(default=None)
    video_bookmarked = models.BooleanField(default=False,null=True)
    article_bookmarked = models.BooleanField(default=False,null=True)

    def __str__(self) -> str:
        return str(self.profile) + str(self.lesson) 
    
    class Meta:
        unique_together=('profile','lesson')
        
        