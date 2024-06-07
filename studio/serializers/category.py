from rest_framework import serializers
from studio.models import Course, Category


class CategorySerializer(serializers.ModelSerializer):
    courses_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'courses_count']

    def get_courses_count(self, obj):
        return obj.courses.count()
