from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from studio.serializers.enrollCourse import EnrollCourseSerializer
from studio.models import Course, User
from django.utils import timezone
from rest_framework.decorators import action
from datetime import datetime
from studio.serializers import UserSerializer


class UserDataViewSet(viewsets.ModelViewSet):               
    @action(detail=False,methods=['get'])
    def getUserDetails(self,request):
        id = request.user.id
        user_instance = get_object_or_404(User,id=id)
        first_name = user_instance.first_name
        last_name = user_instance.last_name
        email = user_instance.email
        return Response({
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        })

   
    
    
   
