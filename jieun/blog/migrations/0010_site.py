# Generated by Django 4.0.7 on 2022-09-28 17:19

import blog.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_delete_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', blog.fields.ThumbnailImageField(blank=True, null=True, upload_to='photo/%Y/%m')),
                ('url', models.URLField(verbose_name='Site URL')),
            ],
        ),
    ]
