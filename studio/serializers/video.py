from rest_framework import serializers
from studio.models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video_name', 'video_url', 'lesson_id']
