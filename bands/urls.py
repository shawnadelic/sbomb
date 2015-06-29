from django.conf.urls import url
from .views import IndexView, BandView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', BandView.as_view(), name='band'),
]
