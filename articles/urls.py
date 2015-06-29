from django.conf.urls import url
from .views import ArticleView, AllArticlesView, CategoryView

urlpatterns = [
    url(r'^$', AllArticlesView.as_view(), name='all_articles'),
    url(r'^(?P<slug>[\w-]+)/$', ArticleView.as_view(), name='article_view'),
    url(r'^categories/(?P<slug>[\w-]+)/$', CategoryView.as_view(), name='category'),
]
