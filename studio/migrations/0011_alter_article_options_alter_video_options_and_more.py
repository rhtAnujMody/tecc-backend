# Generated by Django 4.2.7 on 2024-06-11 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0010_content_object_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='studio.section'),
        ),
        migrations.AddField(
            model_name='video',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='studio.section'),
        ),
    ]
