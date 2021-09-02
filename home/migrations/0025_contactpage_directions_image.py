# Generated by Django 3.2.6 on 2021-09-02 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0024_auto_20210829_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='directions_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
