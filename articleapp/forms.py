from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        # writer와 created_at은 서버 내에서 설정할 것이다.
        fields = ['title', 'image', 'content']