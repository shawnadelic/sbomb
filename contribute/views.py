from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context
from django.contrib.auth import (authenticate, login as auth_login,
        logout as auth_logout)
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

def login(request):
    if request.user.is_authenticated():
        return redirect('contribute:index')
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
          if user.is_active:
              auth_login(request, user)
              return redirect('contribute:index')
    return render(request, 'contribute/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/contribute/login')

@login_required(login_url='/contribute/login')
def index(request):
    return render(request, 'contribute/home.html', {'form': ArticleForm()})
