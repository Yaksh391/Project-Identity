from django.shortcuts import render
from .models import Person
from .models import Project
# Create your views here.


def Home(request, *args, **kwargs):
    obj = Person.objects.filter(first_name__exact="Yaksh")
    # model = Person.objects.all()
    context = {"person": obj[0]}
    return render(request, 'home.html', context)


def Project_Showcase(request, *args, **kwargs):
    objs = Project.objects.all()
    context = {"projects": objs}
    return render(request, 'project/project_showcase.html', context)
