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
from django.contrib.auth import views as auth_views

import main.views

urlpatterns = [
   # url(r'^contribute/account/login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
   # url(r'^contribute/account/logout/$', auth_views.logout, {'template_name': 'account/logout.html'}, name='logout'),
    url(r'^contribute/account/password_change/$', auth_views.password_change, {'template_name': 'account/password_change_form.html'}, name='password_change'),
    url(r'^contribute/account/password_change/done/$', auth_views.password_change_done, {'template_name': 'account/password_change_done.html'}, name='password_change_done'),
    url(r'^contribute/forgot-password/$', auth_views.password_reset, {'template_name': 'account/password_reset_form.html'}, name='password_reset'),
    url(r'^contribute/account/password_reset/done/$', auth_views.password_reset_done, {'template_name': 'account/password_reset_done.html'}, name='password_reset_done'),
    url(r'^contribute/account/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'account/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'account/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^$', main.views.index, name='index'),
    url(r'^about-us/$', TemplateView.as_view(template_name='main/about_us.html'), name='about_us'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^articles/', include('articles.urls', namespace='articles')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^bands/', include('bands.urls', namespace='bands')),
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
    url(r'^contribute/', include('contribute.urls', app_name='contribute', namespace='contribute')),
] + static.static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
