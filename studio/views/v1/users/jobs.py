from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from studio.serializers.jobs import JobsSerializer
from studio.models import Jobs
from django.utils import timezone
from rest_framework.decorators import action
from django.db.models import Q


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    
    def get_serializer_context(self):
        context= super().get_serializer_context()
        context['profile'] = self.request.user.profile
        return context
    
    @action(detail=False, methods=['get'])
    def filter_jobs(self, request):
        skills = request.query_params.get("skills", [])
        experience = request.query_params.get("experience", "")
        location = request.query_params.get("location", "")

        filtered_jobs = Jobs.objects.filter(
            Q(Required_skills__icontains=skills) | Q(job_title__icontains=skills),
            Experience__icontains=experience,
            Location__icontains=location
        )

        serializer = JobsSerializer(filtered_jobs, many=True,context={'profile': self.request.user.profile})
        return Response(serializer.data)

    
    
    
   
