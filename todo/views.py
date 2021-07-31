from django.forms import widgets
from django.shortcuts import redirect, render
from django import forms
from django.utils.regex_helper import Choice
from .models import Questions, Tasks , Answers
from .forms import todo_enter , proc_form
# Create your views here.

def index(request):
    print(request.session)
    form = todo_enter()
    render_task = Tasks.objects.all()
    question_render = Questions.objects.all()
    print(request.POST)
    if request.method == 'POST':
        form = todo_enter(request.POST)
        try:                                 ## avoids error when their is no delete in post request
          if request.POST['delete'] != None:
             Tasks.objects.get(id=request.POST['delete']).delete()
             render_task = Tasks.objects.all()
        except Exception as e:
            print(e)
            pass
        
        if form.is_valid():
            form.save(commit=False)
            request.session['tasken'] = form.cleaned_data['todo']
            return redirect(proc)
            
        
           
        render_task = Tasks.objects.all()
        #question = Questions()
    return render(request, 'index.html', {'task': render_task, 'question':question_render , 'form':form})



def proc(request):
    #form = proc()
    ques = Questions.objects.all().values_list('id','question')
    quesl = Questions.objects.all().values_list('question')
    #ans = Answers.objects.all().values_list('question__id', 'answers')
    
    for z in ques:
        ans = Answers.objects.filter(question__id=z[0]).values_list('points', 'answers')
        proc_form.base_fields[z[1]] = forms.MultipleChoiceField(choices=ans, widget=forms.RadioSelect)
    
    form = proc_form()
    print(ques,ans)


    #class QuizForm(forms.Form):
    #def __init__(self, data, questions, *args, **kwargs):
    #    self.questions = questions
    #    for question in questions:
    #        field_name = "question_%d" % question.pk
    #        choices = []
    #        for answer in question.answer_set().all():
    #            choices.append((answer.pk, answer.answer,))
    #        ## May need to pass some initial data, etc:
    #        field = forms.ChoiceField(label=question.question, required=True, 
    #                                  choices=choices, widget=forms.RadioSelect)
    #    return super(QuizForm, self).__init__(data, *args, **kwargs)




    return render(request, 'login.html' , {'form':form} )




def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')    