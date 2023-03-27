# Generated by Django 4.1.3 on 2023-03-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_person_header_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction_description', models.TextField(default='', help_text='Provide an introduction on the home page!')),
            ],
        ),
    ]
