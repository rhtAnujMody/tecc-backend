from rest_framework import serializers
from  studio.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title','description','thumbnail','category_id','duration','profile','instructor_name','instructor_signature']
        
        

