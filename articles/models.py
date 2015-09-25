import datetime
from base64 import urlsafe_b64encode as url_encode
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Article(models.Model):
    DRAFT, SUBMITTED, PUBLISHED = range(3)
    STATUSES = (
        (DRAFT, 'Draft'),
        (SUBMITTED, 'Submitted'),
        (PUBLISHED, 'Published'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, unique=True)
    body = RichTextField(blank=True)
    pub_date = models.DateTimeField("Publish date", db_index=True, editable=True, default=datetime.datetime.now)
    author = models.ForeignKey(User, related_name='article_author', null=True, blank=True)
    editor = models.ForeignKey(User, related_name='article_editor', null=True, blank=True)
    status = models.IntegerField(choices=STATUSES, default=DRAFT)
    categories = models.ManyToManyField('Category', blank=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to="articles/%Y/%m/%d", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.title == '':
            raise ValidationError
        if self.slug and self.slug != '':
            if Article.objects.filter(slug=self.slug).exists():
                raise ValidationError
        else:
            self.slug = None
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return '/articles/%s' % self.slug

    def preview_hash(self):
        return url_encode(str(self.id))

    class Meta:
        permissions = (('can_publish', 'Can publish articles'),)

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    description = models.TextField()

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Categories"


