# Generated by Django 3.2.6 on 2021-10-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_auto_20211005_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionspage',
            name='subtitle_calendar',
            field=models.CharField(default='Aankomende sessies', max_length=64, verbose_name='ondertitel'),
        ),
    ]
