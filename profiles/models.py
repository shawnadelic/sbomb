from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = RichTextField(blank=True)
    website = models.URLField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.user.first_name
