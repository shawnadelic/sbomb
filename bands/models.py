from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    bandcamp = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="articles/%Y/%m/%d", null=True)
    description = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)
