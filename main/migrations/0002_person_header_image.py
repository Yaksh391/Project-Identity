# Generated by Django 4.1.3 on 2022-11-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='header_image',
            field=models.ImageField(default='', upload_to='personalInformation/'),
        ),
    ]