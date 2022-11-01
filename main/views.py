from django.shortcuts import render

# Create your views here.


def Home(request, *args, **kwargs):
    context = {}
    return render(request, 'base/base.html', context)
