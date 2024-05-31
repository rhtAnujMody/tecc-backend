from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from studio.serializers.lesson import LessonSerializer
from studio.models import Lesson
from rest_framework.decorators import action
from django.db.models import IntegerField
from django.db.models.functions import Cast


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self):
        return Lesson.objects.filter(course_id=self.kwargs['course_pk']).order_by(Cast('sequence', IntegerField()))

    def get_serializer_context(self):
        return {'course_id': self.kwargs['course_pk']}
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['profile'] = self.request.user.profile
        return context
    
    @action(detail=False,methods=['get'])
    def getAllCourseLessons(self,request,pk=None):
        AllLessons = Lesson.objects.all()
        serializer = LessonSerializer(AllLessons,many=True,context={'profile': self.request.user.profile})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=False,methods=['get'])
    def getSingleLesson(self,request,pk=None):
        lesson_id = request.query_params.get("lesson_id")
        SingleLesson = get_object_or_404(Lesson, id=lesson_id)
        serializer = LessonSerializer(SingleLesson,context={'profile':self.request.user.profile})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=False,methods=['get'])
    def getQuiz(self,request,pk=None):
        lesson = request.query_params.get("lesson_id")
        get_lesson = get_object_or_404(Lesson,id=lesson)
        quiz = get_lesson.quiz_schema
        return Response(quiz,status=status.HTTP_200_OK)
        
        

    
    

