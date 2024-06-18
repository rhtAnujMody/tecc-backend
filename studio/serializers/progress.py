from rest_framework import serializers
from studio.models.progress import ArticleProgress, QuizProgress, VideoProgress

class ArticleProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleProgress
        fields = ['profile', 'article', 'is_completed']

class VideoProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoProgress
        fields = ['profile', 'video', 'is_completed']

class QuizProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizProgress
        fields = ['profile', 'quiz', 'is_completed']