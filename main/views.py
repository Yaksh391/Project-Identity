from django.shortcuts import render
from .models import Person
from .models import Project
from .models import HomePage, AboutPageTimelineEvent
# Create your views here.


def Home(request, *args, **kwargs):
    obj = Person.objects.filter(first_name__exact="Yaksh")
    homeinfo = HomePage.objects.first()
    # model = Person.objects.all()
    context = {"person": obj[0], "homepageinfo": homeinfo}
    return render(request, 'home.html', context)


def About(request, *args, **kwargs):
    obj = Person.objects.filter(first_name__exact="Yaksh")
    timeline_events = AboutPageTimelineEvent.objects.all().order_by('-Event_date_op')
    # model = Person.objects.all()
    context = {
        "person": obj[0],
        "timeline_events": timeline_events,
    }
    return render(request, 'about.html', context)


def Project_Showcase(request, *args, **kwargs):
    objs = Project.objects.all()
    context = {"projects": objs}
    return render(request, 'project/project_showcase.html', context)


def Project_Preview(request, title, *args, **kwargs):
    obj = Project.objects.get(title=title.title())
    context = {"project": obj}
    return render(request, 'project/project_preview.html', context)


def Links(request, *args, **kwargs):
    context = {}
    return render(request, 'base/links.html', context)
