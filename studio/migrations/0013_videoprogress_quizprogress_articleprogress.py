# Generated by Django 4.2.7 on 2024-06-12 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0012_alter_quiz_options_quiz_order_quiz_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_progress', to='studio.profile')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_progress', to='studio.video')),
            ],
        ),
        migrations.CreateModel(
            name='QuizProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_progress', to='studio.profile')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_progress', to='studio.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_progress', to='studio.article')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_progress', to='studio.profile')),
            ],
        ),
    ]
