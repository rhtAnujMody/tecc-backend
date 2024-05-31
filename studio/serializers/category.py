from rest_framework import serializers
from  studio.models import Category
from studio.serializers import CourseSerializer


class CategorySerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['name','courses','id']


