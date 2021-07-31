from datetime import date
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Tasks(models.Model):
    userid = models.CharField(max_length=20)
    todo = models.CharField(max_length=100)
    prio = models.IntegerField()
    dategenrate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo

class Questions(models.Model):
    question = models.CharField(max_length=10000)
    def __str__(self):
        return self.question

class Answers(models.Model):
    answers = models.CharField(max_length=50)
    points = models.IntegerField()
    question = models.ForeignKey("Questions", on_delete=models.CASCADE)
    def __str__(self):
        return (self.answers + "  ||  " + str(self.points) + "  ||  "  +self.question.question)