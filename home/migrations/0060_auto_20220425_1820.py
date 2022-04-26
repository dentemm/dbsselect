# Generated by Django 3.2.6 on 2022-04-25 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0059_homepageimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='team_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='team_text',
            field=models.TextField(null=True),
        ),
    ]