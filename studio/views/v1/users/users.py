from rest_framework import viewsets
from studio.serializers import UserSerializer
from studio.models import User
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False,methods=['get'])
    def getFullName(self,request):
        user_id = request.query_params.get("user_id")
        user_instance = get_object_or_404(User,id=user_id)
        first_name = user_instance.first_name
        last_name = user_instance.last_name
        return Response({
            'first_name': first_name,
            'last_name': last_name,
        })
        
    
    
    
    