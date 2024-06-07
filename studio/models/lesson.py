from django.db import models
from .course import Course
from .common import TimeStampedUUIDModel
from uuid import uuid4
import os
from django.core.exceptions import ValidationError


def validate_pdf_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']

    if not ext.lower() in valid_extensions:
        raise ValidationError('Only PDF files are allowed.')


class Lesson(TimeStampedUUIDModel):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False) 
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='lessons')
    sequence = models.CharField(max_length=255)
    duration = models.CharField(max_length=50,null=True)

    def __str__(self) -> str:
        return self.title