# Generated by Django 3.2.6 on 2022-01-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_delete_sessionspagetestimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relivepage',
            name='info',
            field=models.CharField(default='Lorem ipsum', max_length=512, verbose_name='info tekst'),
        ),
    ]
