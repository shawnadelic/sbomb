from django.conf.urls import url, include
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import password_reset, password_reset_done
from .views import (home, login, logout,
        articles_add, articles_list, articles_preview, articles_edit,
        articles_delete, articles_submit, articles_unsubmit, editor_publish,
        editor_publish_submit)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='contribute/index.html'), name='index'),
    url(r'^home/$', home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^articles/add/$', articles_add, name='articles_add'),
    url(r'^articles/list/$', articles_list, name='articles_list'),
    url(r'^articles/preview/(?P<article_id>.*)$', articles_preview, name='articles_preview'),
    url(r'^articles/edit/(?P<article_id>.*)$', articles_edit, name='articles_edit'),
    url(r'^articles/delete/(?P<article_id>.*)$', articles_delete, name='articles_delete'),
    url(r'^articles/submit/(?P<article_id>.*)$', articles_submit, name='articles_submit'),
    url(r'^articles/unsubmit/(?P<article_id>.*)$', articles_unsubmit, name='articles_unsubmit'),
    url(r'^editor/publish/$', editor_publish, name='editor_publish'),
    url(r'^editor/publish/(?P<article_id>.*)$', editor_publish_submit, name='editor_publish_submit'),
]
