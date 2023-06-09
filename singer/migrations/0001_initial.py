# Generated by Django 4.1.6 on 2023-02-18 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='singer')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profession', models.IntegerField(blank=True, choices=[(0, 'Rock'), (1, 'Pop'), (2, 'Classic'), (3, 'Rap'), (4, 'Djazz')], null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
