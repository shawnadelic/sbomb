from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'contribute/account/login.html')

@login_required(login_url='/contribute/login')
def index(request):
    user = request.user
    auth = "Yes" if user.is_authenticated() else "No"
    perm = str(user.user_permissions)
    context = Context({
    })
    return render(request, 'contribute/account/base.html', context)
