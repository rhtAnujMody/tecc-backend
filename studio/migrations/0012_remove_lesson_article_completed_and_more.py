# Generated by Django 4.2.7 on 2023-12-15 09:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0011_lesson_article_completed_lesson_quiz_completed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='article_completed',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='quiz_completed',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='quiz_marks',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='quiz_result',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='video_completed',
        ),
        migrations.AddField(
            model_name='enrollcourse',
            name='course_progress',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
