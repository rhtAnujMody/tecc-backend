from rest_framework import serializers
from studio.models import Video
from studio.models import Video

class VideoSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    class Meta:
        model = Video
        fields = ['id', 'section', 'video_name', 'video_url', 'order', 'duration', 'type']

    
    def get_type(self, obj):
        return 'video'