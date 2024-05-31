from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from studio.models import Lesson
from django.shortcuts import get_object_or_404
from studio.serializers.lessonCompletion import LessonCompletionSerializer
from studio.models import LessonCompletion
from rest_framework.decorators import action


class LessonCompletionViewSet(viewsets.ModelViewSet):
    queryset = LessonCompletion.objects.all()
    serializer_class = LessonCompletion
    
    @action(detail=False,methods=['post'])
    def Lessontrack(self,request,pk=None):
        profile = request.user.profile
        lesson_id = request.data.get("lesson_id")
        lesson_instance = get_object_or_404(Lesson,id=lesson_id)
        video_completed = request.data.get("video_completed",False)
        article_completed = request.data.get("article_completed",False)
        quiz_completed = request.data.get("quiz_completed",False)
        quiz_marks = request.data.get("quiz_marks",0)
        lessoncompletion = LessonCompletion.objects.filter(profile=profile,lesson=lesson_instance)
        if lessoncompletion.exists():
            return Response({'details':"already exists"},status=status.HTTP_400_BAD_REQUEST)
        
        lessontracker = LessonCompletion.objects.create(profile=profile,
                                                        lesson=lesson_instance,
                                                        video_completed=video_completed,
                                                        article_completed=article_completed,
                                                        quiz_completed=quiz_completed,
                                                        quiz_marks=quiz_marks)
        
        serializer = LessonCompletionSerializer(lessontracker)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    @action(detail=False,methods=['put'])
    def updateLessonTrack(self,request,pk=None):
        profile = request.user.profile
        lesson_id = request.data.get("lesson_id")
        video_completed = request.data.get("video_completed")
        article_completed = request.data.get("article_completed")
        quiz_completed = request.data.get("quiz_completed")
        quiz_marks = request.data.get("quiz_marks")
        video_bookmarked = request.data.get("video_bookmarked")
        article_bookmarked = request.data.get("article_bookmarked")
        lessoncompletion = get_object_or_404(LessonCompletion,profile=profile,lesson=lesson_id)
        lessoncompletion.video_completed = video_completed
        lessoncompletion.article_completed = article_completed
        lessoncompletion.quiz_completed = quiz_completed
        lessoncompletion.quiz_marks = quiz_marks
        lessoncompletion.video_bookmarked = video_bookmarked
        lessoncompletion.article_bookmarked = article_bookmarked
        lessoncompletion.save()
        serializer = LessonCompletionSerializer(lessoncompletion)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    
        
        

    
    

