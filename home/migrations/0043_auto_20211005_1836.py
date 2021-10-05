# Generated by Django 3.2.6 on 2021-10-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_sessionspage_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionspage',
            name='subscribe_link',
            field=models.URLField(default='https://www.google.be', verbose_name='inschrijf link'),
        ),
        migrations.AddField(
            model_name='sessionspage',
            name='subscribe_text',
            field=models.CharField(default='Schrijf je hier in voor een sessie', max_length=64, verbose_name='link test'),
        ),
    ]
