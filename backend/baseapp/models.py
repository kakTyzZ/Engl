from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    createdAt = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    nameRu = models.CharField(max_length=200, null=True, blank=True)
    nameEn = models.CharField(max_length=200, null=True, blank=True)
    
    
    def __str__(self):
        return self.nameRu
    
