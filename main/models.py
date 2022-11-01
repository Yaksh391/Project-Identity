from django.db import models


# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30, default="")
    middle_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    picture = models.ImageField(upload_to='media/')
    picture_background_removed = models.ImageField(upload_to='media/', default="")
    hobbies = models.TextField(default="", help_text="Please separate them by a comma.")
    interests = models.TextField(default="", help_text="Please separate them by a comma.")
    skills = models.TextField(default="", help_text="Please separate them by a comma.")
