from django.shortcuts import render
from articles.models import Article

def index(request):
    featured_articles = Article.objects.filter(status=Article.PUBLISHED).filter(featured=True).order_by('-pub_date')
    recent_articles = Article.objects.filter(status=Article.PUBLISHED).order_by('-pub_date').filter(featured=False)[:6]
    return render(request,'main/index.html',{'featured_articles':featured_articles, 'recent_articles':recent_articles})
