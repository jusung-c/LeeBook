from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    # 1 : 1 관계. 계정이 사라지면 프로필도 사라지도록 설정
    # request.user.profile.nickname으로 바로 접근할 수 있도록 related_name을 설정
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # 미디어 세팅했었으므로 media/profile/이라는 경로에 이미지가 저장되는 것이다.
    image = models.ImageField(upload_to='profile/', null=True)

    # 닉네임이 중복되지 않도록 설정
    nickname = models.CharField(max_length=20, unique=True, null=True)

    message = models.CharField(max_length=100, null=True)
