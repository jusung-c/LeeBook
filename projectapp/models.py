from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)