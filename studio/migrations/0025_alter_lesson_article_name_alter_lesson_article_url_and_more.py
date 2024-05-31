# Generated by Django 4.2.7 on 2024-01-02 11:09

from django.db import migrations, models
import studio.models.lesson


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0024_alter_lesson_article_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='article_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='article_url',
            field=models.FileField(null=True, upload_to='media/', validators=[studio.models.lesson.validate_pdf_extension]),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='quiz_schema',
            field=models.JSONField(null=True),
        ),
    ]