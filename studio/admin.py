from django.contrib import admin
from .models import User, Course, Category, Quiz, EnrollCourse, Video, Article, Section
from .models.progress import VideoProgress

class BookAdmin(admin.ModelAdmin):
    exclude = ('django-auditlog', 'is_staff', 'is_active', 'username', 'user_permissions', 'is_superuser', 'groups', 'last_login', 'duration','is_enrolled','instructor_name', 'profile', 'instructor_signature', 'sequence', 'object_id')

# Register your models here.
admin.site.register(User, BookAdmin)
#admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Course, BookAdmin)
#admin.site.register(Quiz)
admin.site.register(EnrollCourse)
admin.site.register(Video)
admin.site.register(Article)
admin.site.register(Quiz)
admin.site.register(Section)
admin.site.register(VideoProgress)






