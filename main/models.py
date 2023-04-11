from django.db import models

# Create your models here.


class HomePage(models.Model):
    introduction_description = models.TextField(default="", help_text="Provide an introduction on the home page!")


class Person(models.Model):
    first_name = models.CharField(max_length=30, default="")
    middle_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    picture = models.ImageField(upload_to='personalInformation/')
    picture_background_removed = models.ImageField(upload_to='personalInformation/', default="")
    # header_image = models.ImageField(upload_to='personalInformation/', default="")
    hobbies = models.TextField(default="", help_text="Please separate them by a comma.")
    interests = models.TextField(default="", help_text="Please separate them by a comma.")
    skills = models.TextField(default="", help_text="Please separate them by a comma.")


def path_project_title(instance, filename):
    return 'projectInformation/{0}/{1}'.format(instance.title, filename)


def path_service_title(instance, filename):
    return 'serviceInformation/{0}/{1}'.format(instance.title, filename)


def path_academics_title(instance, filename):
    return 'academicInformation/{0}/{1}'.format(instance.title, filename)


class Project(models.Model):
    title = models.CharField(max_length=50, default="",  help_text="Please use title case formatting only")
    cover_description = models.TextField(max_length=400, default="")
    description = models.TextField(max_length=5000, default="")
    references = models.TextField(max_length=1000, default="")
    cover_image = models.ImageField(upload_to=path_project_title, default="")
    image_1 = models.ImageField(upload_to=path_project_title, default="", null=True, blank=True)
    image_2 = models.ImageField(upload_to=path_project_title, default="", null=True, blank=True)
    image_3 = models.ImageField(upload_to=path_project_title, default="", null=True, blank=True)
    image_4 = models.ImageField(upload_to=path_project_title, default="", null=True, blank=True)
    image_5 = models.ImageField(upload_to=path_project_title, default="", null=True, blank=True)
    image_6 = models.ImageField(upload_to=path_project_title, default="", null=True, blank=True)
    image_7 = models.ImageField(upload_to=path_project_title, default="", null=True, blank=True)
    PDF_file = models.FileField(upload_to=path_project_title, default="", null=True, blank=True)
    youtube_video = models.CharField(default="", max_length=40, null=True, blank=True)
    discipline_of_work = models.TextField(default="", help_text="Please separate them by a comma.")


class CommunityService(models.Model):
    title = models.CharField(max_length=50, default="",  help_text="Please use title case formatting only")
    cover_description = models.TextField(max_length=400, default="")
    description = models.TextField(max_length=5000, default="")
    cover_image = models.ImageField(upload_to=path_service_title, default="")
    image_1 = models.ImageField(upload_to=path_service_title, default="", null=True, blank=True)
    image_2 = models.ImageField(upload_to=path_service_title, default="", null=True, blank=True)
    image_3 = models.ImageField(upload_to=path_service_title, default="", null=True, blank=True)
    image_4 = models.ImageField(upload_to=path_service_title, default="", null=True, blank=True)
    image_5 = models.ImageField(upload_to=path_service_title, default="", null=True, blank=True)
    image_6 = models.ImageField(upload_to=path_service_title, default="", null=True, blank=True)
    image_7 = models.ImageField(upload_to=path_service_title, default="", null=True, blank=True)
    youtube_video = models.CharField(default="", max_length=40, null=True, blank=True)


class AcademicAchievement(models.Model):
    title = models.CharField(max_length=50, default="",  help_text="Please use title case formatting only")
    cover_description = models.TextField(max_length=400, default="")
    description = models.TextField(max_length=5000, default="")
    cover_image = models.ImageField(upload_to=path_academics_title, default="")
    image_1 = models.ImageField(upload_to=path_academics_title, default="", null=True, blank=True)
    image_2 = models.ImageField(upload_to=path_academics_title, default="", null=True, blank=True)
    image_3 = models.ImageField(upload_to=path_academics_title, default="", null=True, blank=True)
    youtube_video = models.CharField(default="", max_length=40, null=True, blank=True)


class AboutPageTimelineEvent(models.Model):
    Event_date_op = models.CharField(max_length=50, default="", help_text="Please put in event date.")
    Event_title = models.CharField(max_length=200, default="", help_text="Please put in a exciting title for the event!")
    Event_description = models.TextField(max_length=1000, default="")


class AcademicsPageTimelineEvent(models.Model):
    Event_date_op = models.CharField(max_length=50, default="", help_text="Please put in event date.")
    Event_title = models.CharField(max_length=200, default="", help_text="Please put in a exciting title for the event!")
    Event_description = models.TextField(max_length=1000, default="")
