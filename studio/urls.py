from django.urls import path, include
from studio.views.v1.users.course import CourseViewSet
from studio.views.v1.users.category import CategoryViewSet
from studio.views.v1.users.quiz import QuizViewSet
from studio.views.v1.users.enrollCourse import EnrollCourseViewSet
from studio.views.v1.users.users import UserViewSet
from rest_framework_nested import routers
from studio.views.v1.users.userData import UserDataViewSet
from studio.views.v1.users.video import VideoViewSet
from studio.views.v1.users.article import ArticleViewSet
from studio.views.v1.users.section import SectionViewSet
from studio.views.v1.users.dashboard import DashboardViewSet
from studio.views.v1.users.progress import ProgressViewSet
from studio.views.v1.users.certificate import CertificateViewSet

router = routers.DefaultRouter()
router.register('categories',CategoryViewSet)
router.register('courses',CourseViewSet)
router.register('quiz',QuizViewSet,basename='quiz')
router.register('enrollCourse',EnrollCourseViewSet,basename='enrollCourse')
router.register('users',UserViewSet,basename='users')
router.register('sections',SectionViewSet,basename='All-lessons')
router.register('userData',UserDataViewSet,basename='userData')
router.register('videos', VideoViewSet)
router.register('articles', ArticleViewSet)
router.register('dashboard', DashboardViewSet,basename='dashboard')
router.register('progress', ProgressViewSet,basename='progress')

router.register('certificate', CertificateViewSet,basename='progress')

course_router = routers.NestedDefaultRouter(router,'courses',lookup='course')
course_router.register('sectio',SectionViewSet,basename='certificate')

urlpatterns =router.urls+course_router.urls


