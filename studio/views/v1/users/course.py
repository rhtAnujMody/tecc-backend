from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from studio.serializers.course import CourseSerializer
from studio.models import Course
from django.utils import timezone
from rest_framework.decorators import action
from django.template.loader import render_to_string


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
        
    
    
   
