from django.conf.urls import url
from django.http import HttpResponse

from .views import index, login, logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'login/$', login, name='login'),
    url(r'logout/$', logout, name='logout'),
]
