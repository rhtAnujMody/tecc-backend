from rest_framework import serializers
from studio.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ['id', 'section', 'article_name', 'article_url', 'order', 'type']
    
    def get_type(self, obj):
        return 'article'