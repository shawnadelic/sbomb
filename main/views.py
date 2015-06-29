from django.shortcuts import render
from articles.models import Article

def index(request):
    featured_articles = Article.objects.filter(featured=True).order_by('-pub_date')
    return render(request,'main/index.html',{'featured_articles':featured_articles})
