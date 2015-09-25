from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import TemplateView

from .views import home, login, logout, \
        articles_add, articles_list, articles_preview

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='contribute/index.html'), name='index'),
    url(r'^home/$', home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^articles/add/$', articles_add, name='articles_add'),
    url(r'^articles/list/$', articles_list, name='articles_list'),
    url(r'^articles/preview/(?P<article_id>.*)$', articles_preview, name='articles_preview'),
]
