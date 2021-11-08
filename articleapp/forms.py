from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start',
                                                           'style': 'heigth: auto;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        # writer와 created_at은 서버 내에서 설정할 것이다.
        fields = ['title', 'image', 'project', 'content']