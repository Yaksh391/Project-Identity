# Generated by Django 4.1.3 on 2022-11-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='picture_background_removed',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]
