from django.shortcuts import render
from .models import Person
# Create your views here.


def Home(request, *args, **kwargs):
    model = Person.objects.filter(first_name__exact="Yaksh")
    # model = Person.objects.all()
    context = {"person": model[0]}
    return render(request, 'home.html', context)
