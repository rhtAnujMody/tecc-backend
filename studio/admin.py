from django.contrib import admin
from .models import User, Profile,Course,Category,Lesson,Quiz,EnrollCourse,LessonCompletion,Jobs,AppliedJobs

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(EnrollCourse)
admin.site.register(LessonCompletion)
admin.site.register(Jobs)
admin.site.register(AppliedJobs)






