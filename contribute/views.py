import base64
from base64 import urlsafe_b64encode as url_encode, urlsafe_b64decode as url_decode
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.template import Context
from django.contrib import messages
from django.contrib.auth import (authenticate, login as auth_login,
        logout as auth_logout)
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ArticleForm
from articles.models import Article

@login_required(login_url='/contribute/login')
def articles_preview(request, article_id):
    try:
        article_id = int(url_decode(str(article_id)))
    except (ValueError, TypeError):
        raise Http404("Invalid preview URL") 
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if user.id != article.author.id and not user.has_perm('articles.can_publish'):
        return HttpResponseForbidden("Invalid")
    return render(request, 'contribute/article_preview.html', {'article': article})

def login(request):
    if request.user.is_authenticated():
        return redirect('contribute:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('contribute:home')
    return render(request, 'contribute/login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('/contribute/login')

@login_required(login_url='/contribute/login')
def home(request):
    return render(request, 'contribute/home.html')

@login_required(login_url='/contribute/login')
@permission_required('articles.add_article', raise_exception=True)
def articles_add(request):
    form = ArticleForm()
    if request.method == 'POST':
        post = request.POST.copy()
        if post['action'] == 'save-draft':
            draft = ArticleForm(post)
            if draft.is_valid():
                draft = draft.save(commit=False)
                draft.author = request.user
                draft.save()
                return render(request, 'contribute/articles_add_success.html',
                        {'article': draft})
            else:
                form = ArticleForm(post)
                messages.error(request, draft.errors)
        elif post['action'] == 'submit-for-publication':
            messages.success(request, 'Success: Article submitted')
    return render(request, 'contribute/articles_add.html', {'form': form})

@login_required(login_url='/contribute/login')
@permission_required('articles.add_article', raise_exception=True)
def articles_list(request):
    drafts = Article.objects.filter(author=request.user, status=Article.DRAFT)
    submitted = Article.objects.filter(author=request.user, status=Article.SUBMITTED)
    published = Article.objects.filter(author=request.user, status=Article.PUBLISHED)
    return render(request, 'contribute/articles_list.html',
            { 'drafts': drafts,
              'submitted': submitted,
              'published': published }
            )
