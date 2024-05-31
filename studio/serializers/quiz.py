from rest_framework import serializers
from  studio.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id','lesson','question','quiz_type','option','answer','marks']
        
        

