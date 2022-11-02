from django.db import models
import os

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30, default="")
    middle_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    picture = models.ImageField(upload_to='personalInformation/')
    picture_background_removed = models.ImageField(upload_to='personalInformation/', default="")
    hobbies = models.TextField(default="", help_text="Please separate them by a comma.")
    interests = models.TextField(default="", help_text="Please separate them by a comma.")
    skills = models.TextField(default="", help_text="Please separate them by a comma.")


def upload_path_project(instance, filename):
    return os.path.join(instance, filename)


class Project(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.TextField(max_length=500, default="")
    references = models.TextField(max_length=1000, default="")
    cover_image = models.ImageField(upload_to=upload_path_project, default="")
    image_1 = models.ImageField(upload_to=upload_path_project, default="")
    image_2 = models.ImageField(upload_to=upload_path_project, default="")
    image_3 = models.ImageField(upload_to=upload_path_project, default="")
    image_4 = models.ImageField(upload_to=upload_path_project, default="")
    image_5 = models.ImageField(upload_to=upload_path_project, default="")
    image_6 = models.ImageField(upload_to=upload_path_project, default="")
    image_7 = models.ImageField(upload_to=upload_path_project, default="")
    youtube_video = models.CharField(default="", max_length=40)
    discipline_of_work = models.TextField(default="", help_text="Please separate them by a comma.")

