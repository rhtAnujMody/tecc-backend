from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from studio.serializers.course import CourseSerializer
from studio.models import Course
from rest_framework.decorators import action
from django.db.models import IntegerField
from django.db.models.functions import Cast


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    
    @action(detail=False, methods=['get'], url_path='getCourseDetails/(?P<category>[^/.]+)')
    def getCourseDetails(self, request, category=None):
        course = get_object_or_404(Course, id=category)
        serializer = self.get_serializer(course, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

   
    
    

