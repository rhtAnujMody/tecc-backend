# serializers/section.py
from rest_framework import serializers
from studio.models.section import Section
from studio.models.video import Video
from studio.models.article import Article
from studio.models.quiz import Quiz
from .video import VideoSerializer
from .article import ArticleSerializer
from .quiz import QuizSerializer

class SectionSerializer(serializers.ModelSerializer):
    contents = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = ['id', 'title', 'contents']

    def get_contents(self, obj):
        request = self.context.get('request')
        videos = Video.objects.filter(section=obj).order_by('order')
        articles = Article.objects.filter(section=obj).order_by('order')
        quizzes = Quiz.objects.filter(section=obj).order_by('order')

        video_serializer = VideoSerializer(videos, many=True, context={'request': request})
        article_serializer = ArticleSerializer(articles, many=True, context={'request': request})
        quiz_serializer = QuizSerializer(quizzes, many=True, context={'request': request})

        combined_contents = sorted(
            video_serializer.data + article_serializer.data + quiz_serializer.data,
            key=lambda x: x['order']
        )

        return combined_contents
