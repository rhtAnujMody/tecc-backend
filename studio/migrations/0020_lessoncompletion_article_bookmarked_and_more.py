# Generated by Django 4.2.7 on 2023-12-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0019_alter_enrollcourse_course_completion_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessoncompletion',
            name='article_bookmarked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lessoncompletion',
            name='video_bookmarked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lessoncompletion',
            name='quiz_marks',
            field=models.FloatField(default=None),
        ),
    ]
