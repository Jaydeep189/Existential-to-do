from django.contrib import admin
from .models import Answers, Tasks, Questions
# Register your models here.
#admin.site.register(Tasks)
#admin.site.register(Questions)
admin.register(Tasks, Questions, Answers)(admin.ModelAdmin)