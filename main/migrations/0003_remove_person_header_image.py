# Generated by Django 4.1.3 on 2022-11-15 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_person_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='header_image',
        ),
    ]