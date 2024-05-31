from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from studio.serializers.enrollCourse import EnrollCourseSerializer
from studio.models import Course,EnrollCourse
from django.utils import timezone
from rest_framework.decorators import action
from datetime import datetime


class EnrollCourseViewSet(viewsets.ModelViewSet):
    queryset = EnrollCourse.objects.all()
    serializer_class = EnrollCourse
    
    @action(detail=False, methods=['post'])
    def enroll(self,request,*args, **kwargs):
        course_id = request.data.get("course_id")
        course = get_object_or_404(Course,id=course_id)
        profile = request.user.profile
        
        enrollment = EnrollCourse.objects.filter(profile=profile,course_id=course)
        if enrollment.exists():
            return Response({'detail':'User is already enrolled in the course'},status=status.HTTP_400_BAD_REQUEST)
        
        
        enroll_course = EnrollCourse.objects.create(profile=profile,
                                    course_id=course,
                                    is_enrolled=True,
                                    is_CourseStarted=False,
                                    is_CourseCompleted=False)
        
        serializer = EnrollCourseSerializer(enroll_course)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
                    
    @action(detail=False,methods=['get'])
    def getEnrolledCourse(self,request):
        profile = request.user.profile
        EnrolledCourse = EnrollCourse.objects.filter(profile=profile)
        serializer = EnrollCourseSerializer(EnrolledCourse,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=False,methods=['get'])
    def getCourseprogress(self,request):
        profile = request.user.profile
        course_id = request.query_params.get("course_id")
        EnrolledCourse = EnrollCourse.objects.filter(profile=profile,course_id=course_id)
        serializer = EnrollCourseSerializer(EnrolledCourse,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=False,methods=['put'])
    def updateIsCourseStarted(self,request,pk=None):
        profile = request.user.profile
        course_id = request.data.get("course_id")
        CourseInstance = get_object_or_404(EnrollCourse,profile=profile,course_id=course_id)
        CourseInstance.is_CourseStarted = True
        CourseInstance.save()
        serializer = EnrollCourseSerializer(CourseInstance)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=False,methods=['get'])
    def getStartedCourse(self,request):
        course_id = request.query_params.get('course_id')
        profile = request.user.profile
        courses = EnrollCourse.objects.filter(profile=profile,course_id=course_id)
        serializer = EnrollCourseSerializer(courses,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    @action(detail=False,methods=['put'])
    def updateIsCourseCompleted(self,request,pk=None):
        profile = request.user.profile
        course_id = request.data.get("course_id")
        CourseInstance = get_object_or_404(EnrollCourse,profile=profile,course_id=course_id)
        CourseInstance.is_CourseCompleted = True
        if not CourseInstance.course_completion_date:
            CourseInstance.course_completion_date = datetime.now()
        CourseInstance.save()
        serializer = EnrollCourseSerializer(CourseInstance)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    @action(detail=False,methods=['put'])
    def updateCourseProgress(self,request,pk=None):
        profile = request.user.profile
        course_id = request.data.get("course_id")
        course_progress_data = request.data.get('course_progress')
        total_chapter_update = request.data.get('total_chapter')
        completed_chapter_update = request.data.get('completed_chapter')
        course_progress_instance = get_object_or_404(EnrollCourse,profile=profile,course_id=course_id)
        course_progress_instance.course_progress = course_progress_data
        course_progress_instance.total_chapter = total_chapter_update
        course_progress_instance.completed_chapter = completed_chapter_update
        course_progress_instance.save()
        serializer = EnrollCourseSerializer(course_progress_instance)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
        
        
        
    
    
   
