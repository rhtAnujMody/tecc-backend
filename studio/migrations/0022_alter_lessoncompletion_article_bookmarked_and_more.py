# Generated by Django 4.2.7 on 2023-12-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0021_enrollcourse_completed_chapter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessoncompletion',
            name='article_bookmarked',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='lessoncompletion',
            name='video_bookmarked',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
