# Generated by Django 4.2.7 on 2024-06-10 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0007_alter_category_options_alter_content_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='object_id',
        ),
    ]
