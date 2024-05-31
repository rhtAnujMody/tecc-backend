from rest_framework import serializers
from studio.models import EnrollCourse,Course


class EnrollCourseSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    instructor_name = serializers.SerializerMethodField()
    instructor_signature = serializers.SerializerMethodField()
    class Meta:
        model=EnrollCourse
        fields = ['id','title','profile','thumbnail','course_id','course_progress','is_enrolled','is_CourseStarted','is_CourseCompleted','enrollment_date','course_completion_date','instructor_name','instructor_signature','total_chapter','completed_chapter']
        
        
    def get_title(self, obj):
        return obj.course_id.title
    
    def get_thumbnail(self, obj):
        return obj.course_id.thumbnail.url
    
    def get_instructor_name(self,obj):
        return obj.course_id.instructor_name
    
    def get_instructor_signature(self,obj):
        return obj.course_id.instructor_signature.url