from django import forms
from django.forms import fields, widgets
from .models import Answers, Tasks

class todo_enter(forms.ModelForm):
    todo = forms.CharField(max_length=100  ,widget=forms.TextInput(attrs={'type':"text" ,'class':"task-input" ,'name':"task" , 'placeholder':"Task"}))
    #todo = forms.CharField(max_length=100)
    
    class Meta:
        model = Tasks
        fields = ['todo']

class proc_form(forms.Form):
    quesid = forms.CharField(max_length=20 ,  required=False , widget= widgets.HiddenInput )
