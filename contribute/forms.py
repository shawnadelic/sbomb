from django import forms
from articles.models import Article
from ckeditor.widgets import CKEditorWidget

class ArticleForm(forms.ModelForm):
    #body = forms.CharField(widget=CKEditorWidget(config_name='default'))
    body = forms.CharField(widget=CKEditorWidget(config_name='contributor_editor'))
    class Meta:
        model = Article
        fields = ['title', 'body', 'image']
