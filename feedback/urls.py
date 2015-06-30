from django.conf.urls import url
from .views import submit

urlpatterns = [
    url(r'^$', submit, name='submit'),
]
