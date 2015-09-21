from django.conf.urls import url
from django.http import HttpResponse

from .views import index, home, login, logout, \
        articles_add, articles_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^home/$', home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^articles/add/$', articles_add, name='articles_add'),
    url(r'^articles/list/$', articles_list, name='articles_list'),
]
