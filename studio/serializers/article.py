from rest_framework import serializers
from studio.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'article_name', 'article_url', 'is_article_completed', 'lesson_id']
