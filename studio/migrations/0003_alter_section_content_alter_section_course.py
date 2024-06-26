# Generated by Django 4.2.7 on 2024-06-09 08:53

from django.db import migrations, models
import django.db.models.deletion
import studio.models.section


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0002_alter_section_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='content',
            field=models.CharField(default=studio.models.section.get_default_section, max_length=255),
        ),
        migrations.AlterField(
            model_name='section',
            name='course',
            field=models.ForeignKey(default=studio.models.section.get_default_course, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='studio.course'),
        ),
    ]
