from rest_framework import serializers
from django.apps import apps
from studio.models import Lesson
from studio.serializers.video import VideoSerializer
from studio.serializers.article import ArticleSerializer
#from studio.serializers.quiz import QuizSerializer

class LessonSerializer(serializers.ModelSerializer):
   videos = VideoSerializer(many=True, read_only=True)
   #articles = ArticleSerializer(many=True, read_only=True)
    #quizzes = QuizSerializer(many=True, read_only=True)
   #Lesson.objects.filter(quiz_schema__isnull=True).update(quiz_schema={})
   class Meta:
      model = Lesson
      fields = ['id','title','content','course_id','sequence','duration', 'videos']
          
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
      

