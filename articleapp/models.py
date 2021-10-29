from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    # SET_NULL은 회원이 탈퇴해도 사라지지 않고 주인없는 글 NULL로 남겨둔다는 의미 -> null=True 설정 필수
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)