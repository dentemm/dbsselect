# Generated by Django 3.2.6 on 2022-08-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0069_auto_20220801_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='supporting_partners',
            field=models.CharField(default='Supporting partners', max_length=128),
        ),
    ]