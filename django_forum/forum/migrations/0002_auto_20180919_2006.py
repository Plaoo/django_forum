# Generated by Django 2.0.5 on 2018-09-19 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='father_discussion',
            new_name='section_membership',
        ),
    ]
