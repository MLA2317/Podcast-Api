# Generated by Django 4.1.6 on 2023-04-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypodcast', '0007_playlist_playmusic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Playmusic',
            new_name='PlaylistItem',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='media/category'),
        ),
    ]
