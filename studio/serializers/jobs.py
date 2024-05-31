from rest_framework import serializers
from studio.models import Jobs


class JobsSerializer(serializers.ModelSerializer):
    is_applied = serializers.SerializerMethodField()
    class Meta:
        model = Jobs
        fields = ['id','job_title','thumbnail','Location','Service_type','Industry','Experience','Required_skills','Compensation','is_applied']
            
    def get_is_applied(self,obj):
        profile = self.context.get('profile')
        applied_job = obj.appliedjobs_set.filter(profile=profile).first()
        return applied_job.is_applied if applied_job else False
        
        
        
        

