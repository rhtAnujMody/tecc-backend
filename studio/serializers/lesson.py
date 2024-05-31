from rest_framework import serializers
from django.apps import apps
from studio.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
   video_completed = serializers.SerializerMethodField()
   article_completed = serializers.SerializerMethodField()
   quiz_completed = serializers.SerializerMethodField()
   quiz_marks = serializers.SerializerMethodField()
   video_bookmarked = serializers.SerializerMethodField()
   article_bookmarked = serializers.SerializerMethodField()
   Lesson.objects.filter(quiz_schema__isnull=True).update(quiz_schema={})
   class Meta:
      model = Lesson
      fields = ['id','title','content','course_id','video_name','video_url','article_name','article_url','sequence','duration','quiz_schema','video_completed','article_completed','quiz_completed','quiz_completed','quiz_marks','video_bookmarked','article_bookmarked']
          
   def get_video_completed(self,obj):
      profile = self.context.get('profile')
      lesson_completion = obj.lessoncompletion_set.filter(profile=profile).first()
      return lesson_completion.video_completed if lesson_completion else False
   
   def get_article_completed(self,obj):
      profile = self.context.get('profile')
      lesson_completion = obj.lessoncompletion_set.filter(profile=profile).first()
      return lesson_completion.article_completed if lesson_completion else False
   
   def get_quiz_completed(self,obj):
      profile = self.context.get('profile')
      lesson_completion = obj.lessoncompletion_set.filter(profile=profile).first()
      return lesson_completion.quiz_completed if lesson_completion else False
   
   def get_quiz_marks(self,obj):
      profile = self.context.get('profile')
      lesson_completion = obj.lessoncompletion_set.filter(profile=profile).first()
      return lesson_completion.quiz_marks if lesson_completion else False
   
   def get_video_bookmarked(self,obj):
      profile = self.context.get('profile')
      lesson_completion = obj.lessoncompletion_set.filter(profile=profile).first()
      return lesson_completion.video_bookmarked if lesson_completion else False
   
   def get_article_bookmarked(self,obj):
      profile = self.context.get('profile')
      lesson_completion = obj.lessoncompletion_set.filter(profile=profile).first()
      return lesson_completion.article_bookmarked if lesson_completion else False
      

