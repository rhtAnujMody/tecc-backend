# Generated by Django 4.2.7 on 2023-12-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0008_remove_course_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_completed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]