from django.shortcuts import render
from .models import Person
from .models import Project, CommunityService, AcademicAchievement
from .models import HomePage, TravelMap
from .models import AboutPageTimelineEvent, AcademicsPageTimelineEvent
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


def Service_Showcase(request, *args, **kwargs):
    objs = CommunityService.objects.all()
    context = {"CommunityServices": objs}
    return render(request, 'service/service_showcase.html', context)


def Project_Preview(request, title, *args, **kwargs):
    obj = Project.objects.get(title=title.title())
    context = {"project": obj}
    return render(request, 'project/project_preview.html', context)


def Service_Preview(request, service_title, *args, **kwargs):
    obj = CommunityService.objects.get(title=service_title.title())
    context = {"CommunityService": obj}
    return render(request, 'service/service_preview.html', context)


def Academic_Preview(request, academic_title, *args, **kwargs):
    obj = AcademicAchievement.objects.get(title=academic_title.title())
    context = {"Achievement": obj}
    return render(request, 'academics/academics_preview.html', context)


def Links(request, *args, **kwargs):
    context = {}
    return render(request, 'base/links.html', context)


def Academics(request, *args, **kwargs):
    timeline_events = AcademicsPageTimelineEvent.objects.all().order_by('-Event_date_op')
    academic_achievements = AcademicAchievement.objects.all()
    context = {
        "timeline_events": timeline_events,
        "academic_achievements": academic_achievements,
    }
    return render(request, 'academics/academics.html', context)


def Travel(request, *args, **kwargs):
    Maps = TravelMap.objects.first()
    context = {
        "Maps": Maps
    }
    return render(request, 'travel/travel.html', context)