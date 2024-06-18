from rest_framework import viewsets
from studio.models import Video
from studio.serializers.video import VideoSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
