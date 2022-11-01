# Generated by Django 4.1.3 on 2022-11-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('middle_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('picture', models.ImageField(upload_to='uploads/')),
                ('picture_background_removed', models.ImageField(default='', upload_to='uploads/')),
                ('hobbies', models.TextField(default='', help_text='Please separate them by a comma.')),
                ('interests', models.TextField(default='', help_text='Please separate them by a comma.')),
                ('skills', models.TextField(default='', help_text='Please separate them by a comma.')),
            ],
        ),
    ]
