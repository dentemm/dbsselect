# Generated by Django 3.2.6 on 2022-12-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0071_auto_20221214_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='press',
            name='content_de',
            field=models.CharField(default='', max_length=512, verbose_name='korte inhoud (DE)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='press',
            name='content_fr',
            field=models.CharField(default='', max_length=512, verbose_name='korte inhoud (FR)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='press',
            name='content_nl',
            field=models.CharField(default='', max_length=512, verbose_name='korte inhoud (NL)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='press',
            name='title_de',
            field=models.CharField(default='', max_length=128, verbose_name='titel (DE)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='press',
            name='title_fr',
            field=models.CharField(default='', max_length=128, verbose_name='titel (FR)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='press',
            name='title_nl',
            field=models.CharField(default='', max_length=128, verbose_name='titel (NL)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='press',
            name='content',
            field=models.CharField(max_length=512, verbose_name='korte inhoud (EN)'),
        ),
        migrations.AlterField(
            model_name='press',
            name='title',
            field=models.CharField(max_length=128, verbose_name='titel (EN)'),
        ),
    ]