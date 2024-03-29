# Generated by Django 3.2.6 on 2022-01-07 12:35

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_alter_aboutpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='content',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='titel', max_length=64)), ('content', wagtail.core.blocks.TextBlock(label='tekst', max_length=512)), ('image', wagtail.images.blocks.ImageChooserBlock(label='afbeelding', required=False)), ('gallery', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), label='foto gallerij', required=False)), ('video', wagtailmedia.blocks.VideoChooserBlock(label='video', required=False))]))], null=True),
        ),
    ]
