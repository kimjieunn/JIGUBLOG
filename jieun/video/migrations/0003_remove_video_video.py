# Generated by Django 4.0.7 on 2022-09-28 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_video_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
    ]
