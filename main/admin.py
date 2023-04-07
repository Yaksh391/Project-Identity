from django.contrib import admin
from main import models


# Register your models here.

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name']


@admin.register(models.Project)
class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]


@admin.register(models.HomePage)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AboutPageTimelineEvent)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['Event_date_op', 'Event_title']


@admin.register(models.AcademicsPageTimelineEvent)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['Event_date_op', 'Event_title']


@admin.register(models.CommunityService)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["title"]
