# Generated by Django 4.1.3 on 2023-04-11 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_pdf_file_project_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='youtube_video',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]
