from django.shortcuts import render
from django.views import generic
from .models import UserProfile

class ProfileView(generic.DetailView):
    template_name = 'profiles/profile.html'
    model = UserProfile
    context_object_name = 'user_profile'
