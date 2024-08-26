from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
# the main basic idea of creating TODo application is to know about CRUD operations
# create, read, update, delete

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updates_at')
    #The above is to filter all the tasks that are not completed and also store the tasks in order of the time they created
    # in order_by if we use '-' before the feild name it will filter in descending order, otherwise in ascending order
    context = {
        'tasks_': tasks, 
    }
    # as we want the completed tasks to be printed on home.html, so we need to use context dictionary
    return render(request, 'home.html', context)
    # in home page we want the tasks to be printed so we pass context in reder