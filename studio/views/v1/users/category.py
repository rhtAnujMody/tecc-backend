from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from studio.serializers import CategorySerializer
from studio.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
