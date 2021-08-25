# Generated by Django 3.2.6 on 2021-08-25 19:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0020_aboutpage_sessionspage_sessionspagetestimonial_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Datum')),
                ('link', models.URLField(max_length=64, verbose_name='Info')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Sessie',
                'verbose_name_plural': 'Sessies',
            },
        ),
    ]
