from rest_framework import viewsets
from studio.models import Article
from studio.serializers.article import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
