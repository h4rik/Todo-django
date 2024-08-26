from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task_of_user = request.POST['task']
    #the task inside post is "name" of the input field, which is in home.html
    Task.objects.create(task=task_of_user)
    # By using the above task will be created in database that is we can see in admin
    #In task=task_of_user, task is the feild name in models.py and Task is the table name
    #return HttpResponse('The form is submitted')
    # we dont want http reponse, we want to get the back to home page after adding the task and also the task should be appeared on the home page
    return redirect('home')
    # home is the name of the path present in urls patterns of urls.py of todo_main

def mark_as_done(request, pk):
    # the mark_as_done as takes primary key in urls.py as well so need to pass pk in the above function as well.
    #return HttpResponse(pk)
    task = get_object_or_404(Task, pk=pk)
    # get_object_or_404 functions means if the function exists in the database, it fetches or else it returns 404 error 
    # Task is the class or table name and in pK=pk, pk before = means the feild name of the Task module and pk after = means it is the dynamic value generated 
    # so get_object_or_404 gets the task based on pk number 
    task.is_completed = True
    # here as we set to TRUE it goes to completed_tasks in views.py and then task is added to completed tasks in home page
    task.save()
    return redirect('home')
    #return HttpResponse(task)

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        #print(new_task)
        # the task is from the input tag of edit_task.html 
        #  <input type="text" name = "task" class="form-control" placeholder="Add a task" value="{{ get_task.task }}">
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else: # HERE IT IS GET METHOD
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)
    # as we want the task to be edited in a page, we need edit_task.html
    # POST means when we update or add or delete something inside the database, the POST request is sent to the server
    # GET means when we reload the page or loading the html template that is called as GET request and request is send to the server

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')