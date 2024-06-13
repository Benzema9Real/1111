from django.db import models

class Task(models.Model):
    title = models.CharField('Заголовок',max_length=300)
    description = models.TextField('Oписание', blank=True)
    completed = models.BooleanField('завершен',False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
