from rest_framework import serializers
from studio.models import Course, EnrollCourse, Video, Section
from studio.serializers.section import SectionSerializer

class CourseSerializer(serializers.ModelSerializer):
    is_enrolled = serializers.SerializerMethodField()
    is_CourseCompleted = serializers.SerializerMethodField()
    count_of_lectures = serializers.SerializerMethodField()
    course_progress = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    sections = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'category_name', 'title', 'description', 'thumbnail', 'credit', 'is_mandatory', 'is_certification_course', 'certification_course_url', 'is_enrolled', 'is_CourseCompleted', 'count_of_lectures', 'course_progress', 'sections']

    def get_is_enrolled(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return EnrollCourse.objects.filter(profile__user=request.user, course_id=obj).exists()
        return False

    def get_category_name(self, obj):
        if obj.category:
            return obj.category.name
        return None

    def get_course_progress(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            try:
                enrollment = EnrollCourse.objects.get(profile__user=request.user, course_id=obj)
                return enrollment.course_progress
            except EnrollCourse.DoesNotExist:
                return False
        return False

    def get_is_CourseCompleted(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            try:
                enrollment = EnrollCourse.objects.get(profile__user=request.user, course_id=obj)
                return enrollment.is_CourseCompleted
            except EnrollCourse.DoesNotExist:
                return False
        return False
    
    def get_count_of_lectures(self, obj):
        # Count all videos related to sections of the given course
        return Video.objects.filter(section__course=obj).count()
    
    def get_sections(self, obj):
        request = self.context.get('request')
        sections = Section.objects.filter(course=obj).order_by('order')
        return SectionSerializer(sections, many=True, context={'request': request}).data