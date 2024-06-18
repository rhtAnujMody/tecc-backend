from django.db import models
from studio.models import Profile
from studio.models import Article, Video, Quiz

class ArticleProgress(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='article_progress')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='user_progress')
    is_completed = models.BooleanField(default=False)

class VideoProgress(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='video_progress')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='user_progress')
    is_completed = models.BooleanField(default=False)

class QuizProgress(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='quiz_progress')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='user_progress')
    is_completed = models.BooleanField(default=False)
