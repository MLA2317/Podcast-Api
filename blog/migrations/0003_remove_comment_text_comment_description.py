# Generated by Django 4.1.6 on 2023-02-19 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.AddField(
            model_name='comment',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
