# Generated by Django 3.2.6 on 2021-10-05 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_alter_homepage_about_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionspage',
            name='video',
            field=models.URLField(default='https://storage.googleapis.com/coverr-main/mp4/Mt_Baker.mp4', verbose_name='video link'),
        ),
    ]
