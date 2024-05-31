from rest_framework import serializers
from studio.models import AppliedJobs


class AppliedJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedJobs
        fields = ['id','profile','job','applied_date','is_applied']
        
        

