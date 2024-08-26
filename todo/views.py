from django.shortcuts import render, redirect
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
