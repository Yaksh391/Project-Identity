"""ProjectIdentity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as mainViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainViews.Home),
    path('projects/', mainViews.Project_Showcase),
    path('projects/<str:title>/', mainViews.Project_Preview),
    path('services/', mainViews.Service_Showcase),
    path('services/<str:service_title>/', mainViews.Service_Preview),
    path('about/', mainViews.About),
    path('links/', mainViews.Links),
    path('academics/', mainViews.Academics),
    path('academics/<str:academic_title>/', mainViews.Academic_Preview),
    path('travel/', mainViews.Travel)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
