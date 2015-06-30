"""sbomb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url, static
from django.contrib import admin
from django.views.generic import TemplateView

import main.views, articles.views

urlpatterns = [
    url(r'^$', main.views.index, name='index'),
    url(r'^about_us/$', TemplateView.as_view(template_name='main/about_us.html'), name='about_us'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contribute/login/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^articles/', include('articles.urls', namespace='articles')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^bands/', include('bands.urls', namespace='bands')),
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
] + static.static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
