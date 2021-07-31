from django import forms
from django.forms import fields, widgets
from .models import Tasks

class todo_enter(forms.ModelForm):
    todo = forms.CharField(max_length=100  ,widget=forms.TextInput(attrs={'type':"text" ,'class':"text" ,'name':"task" , 'placeholder':"Task"}))
    #todo = forms.CharField(max_length=100)
    
    class Meta:
        model = Tasks
        fields = ['todo']