# Generated by Django 4.0.7 on 2022-09-28 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_album_owner_photo_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ('title',), 'verbose_name': 'album_photo', 'verbose_name_plural': 'album_photos'},
        ),
        migrations.AlterModelTable(
            name='photo',
            table='album_photos',
        ),
    ]