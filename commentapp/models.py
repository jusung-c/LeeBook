from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='commnet')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='commnet')

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now=True)

