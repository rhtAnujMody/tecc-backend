from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from studio.models import Course
from studio.serializers.course import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=False, methods=['get'], url_path='byCategory/(?P<category>[^/.]+)')
    def byCategory(self, request, category=None):
        courses = Course.objects.filter(category=category)
        serializer = self.get_serializer(courses, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def getMandatoryCourses(self, request):
        mandatory_courses = Course.objects.filter(is_mandatory=True)
        serializer = self.get_serializer(mandatory_courses, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def getCertificationCourses(self, request):
        mandatory_courses = Course.objects.filter(is_certification_course=True)
        serializer = self.get_serializer(mandatory_courses, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)