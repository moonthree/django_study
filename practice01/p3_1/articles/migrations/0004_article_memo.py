# Generated by Django 3.2.13 on 2022-09-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='memo',
            field=models.CharField(default='', max_length=20),
        ),
    ]
