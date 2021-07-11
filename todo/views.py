from django.shortcuts import render
from .models import Questions, Tasks
# Create your views here.

def index(request):
    render_task = Tasks.objects.all()
    question_render = Questions.objects.all()
    if request.method == 'POST':
        task = Tasks()
        task.todo = request.POST.get('task')
        task.save()
        question = Questions()
    return render(request, 'index.html', {'task': render_task, 'question':question_render})
