# Generated by Django 3.2.6 on 2022-12-16 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0072_auto_20221214_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(blank=True, max_length=128, verbose_name='Naam')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Team foto',
                'verbose_name_plural': "Team foto's",
            },
        ),
    ]