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

@login_required(login_url='/contribute/login')
def articles_delete(request, article_id):
    try:
        article_id = int(url_decode(str(article_id)))
    except (ValueError, TypeError):
        raise Http404("Invalid article ID") 
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if user.id != article.author.id and not user.has_perm('articles.can_publish'):
        return HttpResponseForbidden("Invalid")
    title = article.title
    article.delete()
    messages.success(request, "Article \"{}\" successfully deleted.".format(title))
    return redirect('contribute:articles_list')

@login_required(login_url='/contribute/login')
def articles_submit(request, article_id):
    try:
        article_id = int(url_decode(str(article_id)))
    except (ValueError, TypeError):
        raise Http404("Invalid article ID") 
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if user.id != article.author.id and not user.has_perm('articles.can_publish'):
        return HttpResponseForbidden("Invalid")
    article.status = Article.SUBMITTED
    article.save()
    messages.success(request, "Article \"{}\" successfully submitted for publication.".format(article.title))
    return redirect('contribute:articles_list')

@login_required(login_url='/contribute/login')
def articles_unsubmit(request, article_id):
    try:
        article_id = int(url_decode(str(article_id)))
    except (ValueError, TypeError):
        raise Http404("Invalid article ID") 
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if user.id != article.author.id and not user.has_perm('articles.can_publish'):
        return HttpResponseForbidden("Invalid")
    article.status = Article.DRAFT
    article.save()
    messages.success(request, "Article \"{}\" successfully unsubmitted for publication.".format(article.title))
    return redirect('contribute:articles_list')

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
        else:
            messages.error(request, 'Username and/or password did not match')
    return render(request, 'contribute/login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('/contribute/login')

@login_required(login_url='/contribute/login')
def home(request):
    drafts = Article.objects.filter(author=request.user, status=Article.DRAFT).order_by('-id')
    submitted = Article.objects.filter(author=request.user, status=Article.SUBMITTED).order_by('-id')
    published = Article.objects.filter(author=request.user, status=Article.PUBLISHED).order_by('-id')
    return render(request, 'contribute/home.html',
            { 'drafts': drafts,
              'submitted': submitted,
              'published': published }
            )

@login_required(login_url='/contribute/login')
@permission_required('articles.add_article', raise_exception=True)
def articles_add(request):
    form = ArticleForm()
    if request.method == 'POST':
        post = request.POST.copy()
        draft = ArticleForm(request.POST, request.FILES)
        if draft.is_valid():
            draft = draft.save(commit=False)
            draft.author = request.user
            draft.save()
            messages.success(request, 'Draft successfully saved')
            if post['action'] == 'save-and-close':
                return redirect('contribute:articles_list')
            elif post['action'] == 'save-and-continue':
                return redirect('contribute:articles_edit', article_id = draft.preview_hash())
        else:
            form = ArticleForm(post)

    return render(request, 'contribute/articles_add.html', {'form': form})

@login_required(login_url='/contribute/login')
@permission_required('articles.change_article', raise_exception=True)
def articles_edit(request, article_id):
    try:
        article_id = int(url_decode(str(article_id)))
    except (ValueError, TypeError):
        raise Http404("Invalid article ID") 
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if user.id != article.author.id and not user.has_perm('articles.can_publish'):
        return HttpResponseForbidden("Invalid")

    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if request.method == 'POST':
        post = request.POST.copy()
        if form.is_valid():
            form.save()
            messages.success(request, "Draft successfully saved")
            if post['action'] == 'save-and-close':
                return redirect('contribute:articles_list')
            elif post['action'] == 'save-and-continue':
                article = get_object_or_404(Article, id=article_id)
                form = ArticleForm(instance=article)
        else:
            form = ArticleForm(post)
    return render(request, 'contribute/articles_edit.html', {'form': form})



@login_required(login_url='/contribute/login')
@permission_required('articles.add_article', raise_exception=True)
def articles_list(request):
    drafts = Article.objects.filter(author=request.user, status=Article.DRAFT).order_by('-id')
    submitted = Article.objects.filter(author=request.user, status=Article.SUBMITTED).order_by('-id')
    published = Article.objects.filter(author=request.user, status=Article.PUBLISHED).order_by('-id')
    return render(request, 'contribute/articles_list.html',
            { 'drafts': drafts,
              'submitted': submitted,
              'published': published }
            )

@login_required(login_url='/contribute/login')
@permission_required('articles.can_publish', raise_exception=True)
def editor_publish(request):
    submitted = Article.objects.filter(status=Article.SUBMITTED).order_by('-id')
    return render(request, 'contribute/editor_publish.html', {
            'submitted': submitted,
        })

@login_required(login_url='/contribute/login')
@permission_required('articles.can_publish', raise_exception=True)
def editor_publish_submit(request, article_id):
    return render(request, 'contribute/editor_publish_submit.html')
