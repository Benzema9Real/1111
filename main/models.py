from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    title = models.CharField('Заголовок',max_length=300)
    description = models.TextField('Oписание', blank=True)
    completed = models.BooleanField('завершен',False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    country = models.CharField('Страна', max_length=100, blank=True)
    region = models.CharField('Область', max_length=100, blank=True)
