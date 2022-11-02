from django.contrib import admin
from main import models


# Register your models here.

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Project)
class PersonAdmin(admin.ModelAdmin):
    pass
