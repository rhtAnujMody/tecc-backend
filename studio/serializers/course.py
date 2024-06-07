from rest_framework import serializers
from  studio.models import Course
from studio.serializers.lesson import LessonSerializer
class CourseSerializer(serializers.ModelSerializer):
    sections = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id','title','description','thumbnail','category_id','duration','is_enrolled','instructor_name','instructor_signature', 'sections']
        
        

