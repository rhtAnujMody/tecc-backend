from rest_framework import serializers
from  studio.models import LessonCompletion


class LessonCompletionSerializer(serializers.ModelSerializer):
   class Meta:
      model = LessonCompletion
      fields = ['id','profile','lesson','video_completed','article_completed','quiz_completed','quiz_marks','video_bookmarked','article_bookmarked']
        
        

