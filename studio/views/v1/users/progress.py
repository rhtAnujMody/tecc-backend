from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from studio.models.progress import VideoProgress, ArticleProgress, QuizProgress
from studio.models.enrollCourse import EnrollCourse 
from studio.models import Video, Article, Quiz, Course
from studio.serializers.progress import VideoProgressSerializer, ArticleProgressSerializer, QuizProgressSerializer
from studio.serializers.enrollCourse import EnrollCourseSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = EnrollCourse.objects.all()
    serializer_class = EnrollCourseSerializer

    @action(detail=False, methods=['post'])
    def markVideoCompleted(self, request):
        user = request.user.profile
        video_id = request.data.get("video_id")
        video = get_object_or_404(Video, id=video_id)

        progress, created = VideoProgress.objects.get_or_create(profile=user, video=video)
        progress.is_completed = True
        progress.save()
        self.update_course_progress(user, video.section.course)
        return Response(VideoProgressSerializer(progress).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def markArticleCompleted(self, request):
        user = request.user.profile
        article_id = request.data.get("article_id")
        article = get_object_or_404(Article, id=article_id)

        progress, created = ArticleProgress.objects.get_or_create(profile=user, article=article)
        progress.is_completed = True
        progress.save()

        self.update_course_progress(user, article.section.course)

        return Response(ArticleProgressSerializer(progress).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def markQuizCompleted(self, request):
        user = request.user.profile
        quiz_id = request.data.get("quiz_id")
        quiz = get_object_or_404(Quiz, id=quiz_id)

        progress, created = QuizProgress.objects.get_or_create(profile=user, quiz=quiz)
        progress.is_completed = True
        progress.save()

        self.update_course_progress(user, quiz.section.course)

        return Response(QuizProgressSerializer(progress).data, status=status.HTTP_200_OK)

    def update_course_progress(self, user, course):
        total_items = Video.objects.filter(section__course=course).count() + \
                      Article.objects.filter(section__course=course).count() + \
                      Quiz.objects.filter(section__course=course).count()

        if total_items == 0:
            progress_percentage = 0
        else:
            completed_videos = VideoProgress.objects.filter(profile=user, video__section__course=course, is_completed=True).count()
            completed_articles = ArticleProgress.objects.filter(profile=user, article__section__course=course, is_completed=True).count()
            completed_quizzes = QuizProgress.objects.filter(profile=user, quiz__section__course=course, is_completed=True).count()
            completed_items = completed_videos + completed_articles + completed_quizzes

            progress_percentage = (completed_items / total_items) * 100

        rounded_progress =round(progress_percentage)
        rounded_progress_int = int(rounded_progress)
        course_progress, created = EnrollCourse.objects.get_or_create(profile=user, course_id=course)
        course_progress.course_progress = rounded_progress_int
        course_progress.save()
