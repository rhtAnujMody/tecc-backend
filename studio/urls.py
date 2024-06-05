from django.urls import path, include
from studio.views.v1.users.lesson import LessonViewSet
from studio.views.v1.users.course import CourseViewSet
from studio.views.v1.users.category import CategoryViewSet
from studio.views.v1.users.quiz import QuizViewSet
from studio.views.v1.users.enrollCourse import EnrollCourseViewSet
from studio.views.v1.users.lessonCompletion import LessonCompletionViewSet
from studio.views.v1.users.jobs import JobsViewSet
from studio.views.v1.users.appliedjobs import AppliedJobsViewSet
from studio.views.v1.users.users import UserViewSet
from rest_framework_nested import routers
from studio.views.v1.users.userData import UserDataViewSet

router = routers.DefaultRouter()
router.register('categories',CategoryViewSet)
router.register('courses',CourseViewSet)
router.register('quiz',QuizViewSet,basename='quiz')
router.register('lesson_quiz',LessonViewSet,basename='lesson-quiz')
router.register('enrollCourse',EnrollCourseViewSet,basename='enrollCourse')
router.register('lessonCompletion',LessonCompletionViewSet,basename='lessonCompletion')
router.register('jobs',JobsViewSet,basename='jobs')
router.register('applyjobs',AppliedJobsViewSet,basename='applyjobs')
router.register('users',UserViewSet,basename='users')
router.register('lessons',LessonViewSet,basename='All-lessons')
router.register('userData',UserDataViewSet,basename='userData')

course_router = routers.NestedDefaultRouter(router,'courses',lookup='course')
course_router.register('lessons',LessonViewSet,basename='course-lessons')

urlpatterns =router.urls+course_router.urls


