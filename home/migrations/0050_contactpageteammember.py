# Generated by Django 3.2.6 on 2022-01-07 20:11

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_alter_aboutpage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPageTeamMember',
            fields=[
                ('teammember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.teammember')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='home.contactpage')),
            ],
            options={
                'ordering': ['sort_order'],
            },
            bases=('home.teammember', models.Model),
        ),
    ]
