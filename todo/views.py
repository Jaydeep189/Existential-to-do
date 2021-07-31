from django.forms import widgets
from django.shortcuts import redirect, render
from django import forms
from django.utils.regex_helper import Choice
from .models import Questions, Tasks , Answers
from .forms import todo_enter , proc_form
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/about')
def index(request):
    print(request.session)
    form = todo_enter()
    render_task = Tasks.objects.filter(userid = request.user.id).order_by('-prio')
    question_render = Questions.objects.all()
    print(request.POST)
    if request.method == 'POST':
        form = todo_enter(request.POST)
        try:                                 ## avoids error when their is no delete in post request
          if request.POST['delete'] != None:
             Tasks.objects.get(id=request.POST['delete']).delete()
             render_task = Tasks.objects.filter(userid = request.user.id).order_by('-prio')
        except Exception as e:
            print(e)
            pass
        
        if form.is_valid():
            form.save(commit=False)
            request.session['tasken'] = form.cleaned_data['todo']
            return redirect(proc)
            
        
           
        render_task = Tasks.objects.filter(userid = request.user.id).order_by('-prio')
        #question = Questions()
    return render(request, 'index.html', {'task': render_task, 'question':question_render , 'form':form})
@login_required(login_url='/about')
def proc(request):
    
    ques = Questions.objects.all().values_list('id','question')
    
    for z in ques:
        ans = Answers.objects.filter(question__id=z[0]).values_list('points', 'answers')
        proc_form.base_fields[z[1]] = forms.ChoiceField(choices=ans, widget=forms.RadioSelect)

    form = proc_form()
    if request.method == 'POST':
        print(request.POST)
        form = proc_form(request.POST)
        if form.is_valid():
           sl = []
           for z in ques:
               sl.append(int(form.cleaned_data[z[1]]))
           #print(sum(sl))
           task = Tasks()
           task.prio = sum(sl)
           task.userid = request.user.id
           task.todo = request.session['tasken']
           task.save()

           return redirect(index)
    form = proc_form()


    return render(request, 'login.html' , {'form':form} )


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')    