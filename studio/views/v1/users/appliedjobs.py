from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from studio.serializers.appliedjobs import AppliedJobsSerializer
from studio.models import AppliedJobs,Jobs
from django.utils import timezone
from rest_framework.decorators import action


class AppliedJobsViewSet(viewsets.ModelViewSet):
    queryset = AppliedJobs.objects.all()
    serializer_class = AppliedJobsSerializer
    
    @action(detail=False, methods=['post'])
    def createJobsEntry(self, request):
        profile = request.user.profile
        job_id = request.data.get("job_id")
        job_instance = get_object_or_404(Jobs, id=job_id)
        if AppliedJobs.objects.filter(job=job_instance,profile=profile).exists():
            return Response({'details':"already applied for this job"},status=status.HTTP_400_BAD_REQUEST)
        applyjob = AppliedJobs.objects.create(job=job_instance, profile=profile,is_applied=True)
        serializer = AppliedJobsSerializer(applyjob)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
            
    
    
    
    
    
    
   
