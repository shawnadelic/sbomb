from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'author', 'featured',)
    list_filter = ('status', 'pub_date', 'categories', 'author',)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
