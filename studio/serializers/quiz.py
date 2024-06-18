from rest_framework import serializers
from  studio.models import Quiz
class QuizSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    class Meta:
        model = Quiz
        fields = ['id','section', 'quiz_name', 'quiz_schema', 'is_mandatory', 'order', 'type']
        
    def get_type(self, obj):
        return 'quiz'   

