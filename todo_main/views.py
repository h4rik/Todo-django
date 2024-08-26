from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
# the main basic idea of creating TODo application is to know about CRUD operations
# create, read, update, delete

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updates_at')
    #The above is to filter all the tasks that are not completed and also store the tasks in order of the time they created
    # in order_by if we use '-' before the feild name(updated_at in the above case) it will filter in descending order, otherwise in ascending order
    completed_tasks = Task.objects.filter(is_completed=True)
    #print(completed_tasks)
    # If we refresh the page at http://127.0.0.1:8000/ and we can see the qurey set gets printed in the console which is because we used print() statement above 
    #ex: <QuerySet [<Task: today lunch>, <Task: call to satya uncle at 8 : 30 PM>]>
    context = {
        'tasks_': tasks, 
        'completed_tasks': completed_tasks, 
    }
    # as we want the completed tasks to be printed on home.html, so we need to use context dictionary
    return render(request, 'home.html', context)
    # in home page we want the tasks to be printed so we pass context in reder