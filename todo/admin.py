from django.contrib import admin
from .models import Answers, Tasks, Questions

admin.register(Tasks, Questions, Answers)(admin.ModelAdmin)