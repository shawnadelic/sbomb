from django.conf.urls import url
from django.http import HttpResponse

from .views import index, login

urlpatterns = [
    url(r'^$', index),
    url(r'^login$', login)
]
