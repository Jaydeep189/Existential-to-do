from django.db import models
from django.db.models.base import Model

# Create your models here.
class Tasks(models.Model):
    todo = models.CharField(max_length=100)
    def __str__(self):
        return self.todo

class Questions(models.Model):
    question = models.CharField(max_length=10000)
    def __str__(self):
        return self.question