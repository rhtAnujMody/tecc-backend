from django.http import JsonResponse
from django.db.models import Count, Sum
from studio.models import Course, EnrollCourse, Category
from rest_framework import viewsets
from rest_framework.decorators import action
from studio.serializers.category import CategorySerializer
from studio.serializers.course import CourseSerializer
from rest_framework.permissions import IsAuthenticated

class DashboardViewSet(viewsets.ViewSet): 
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def getDashboardDetails(self, request):
        # Calculate enrolled course count
        user = request.user
        profile = request.user.profile
        enrolled_courses = EnrollCourse.objects.filter(profile=profile)
        enrolled_course_count = enrolled_courses.count()

        # Calculate pending course count
        pending_courses = EnrollCourse.objects.filter(profile=profile, is_CourseCompleted=False)
        pending_course_count = pending_courses.count()

        # Get mandatory courses
        mandatory_courses = Course.objects.filter(is_mandatory=True)
        mandatory_courses_serialized = CourseSerializer(mandatory_courses, many=True).data

        # Get categories
        categories = Category.objects.all()
        categories_serialized = CategorySerializer(categories, many=True).data

        credits = user.credits_earned

        response_data = {
            'enrolled_course_count': enrolled_course_count,
            'pending_course_count': pending_course_count,
            'credits': credits,
            'mandatory_courses': mandatory_courses_serialized,
            'categories': categories_serialized,
        }

        return JsonResponse(response_data, safe=False)
