from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from studio.serializers import QuizSerializer
from studio.models import Quiz
from rest_framework.decorators import action


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
    @action(detail=False,methods=['get'])
    def getQuiz(self,request):
        lesson_id = request.query_params.get("lesson")
        quiz = Quiz.objects.filter(lesson=lesson_id)
        serializer = QuizSerializer(quiz,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
    