# Generated by Django 2.2.9 on 2020-01-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200122_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='partners_title',
            field=models.CharField(default='Partners', max_length=32, verbose_name='Partners'),
        ),
    ]
