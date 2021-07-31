from django.shortcuts import render
from .models import Questions, Tasks
from .forms import todo_enter
# Create your views here.

def index(request):
    print(request.session)
    form = todo_enter()
    render_task = Tasks.objects.all()
    question_render = Questions.objects.all()
    print(request.POST)
    if request.method == 'POST':
        form = todo_enter(request.POST)
        if form.is_valid():
            form.save()
            
        try:                                 ## avoids error when their is no delete in post request
          if request.POST['delete'] != None:
             Tasks.objects.get(id=request.POST['delete']).delete()
             render_task = Tasks.objects.all()
        except Exception as e:
            print(e)
            pass
           
        render_task = Tasks.objects.all()
        #question = Questions()
    return render(request, 'index.html', {'task': render_task, 'question':question_render , 'form':form})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')    