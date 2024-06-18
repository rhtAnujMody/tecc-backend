from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from uuid import uuid4
from .course import Course
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ObjectDoesNotExist

def get_default_course():
    # Try to get the first course
    default_course = Course.objects.first()
    if default_course:
        return default_course.id
    else:
        # Create and return a new default course if none exists
        course = Course.objects.create(title="Default Course", description="This is a default course.")
        return course.id

def get_default_section():
    # Try to get the first section
    default_section = Section.objects.first()
    if default_section:
        return default_section.id
    else:
        # Create and return a new default section if none exists
        course = Course.objects.first()
        if not course:
            course = Course.objects.create(title="Default Course", description="This is a default course.")
        section = Section.objects.create(title="Default Section", course=course, order=0)
        return section.id



class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False) 
    course = models.ForeignKey(Course, related_name='sections', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, unique=True)
    content = models.CharField(max_length=255, null=True)
    order = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = "title"

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']