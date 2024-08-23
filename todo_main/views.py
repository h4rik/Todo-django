from django.http import HttpResponse
from django.shortcuts import render
# the main basic idea of creating TODo application is to know about CRUD operations
# create, read, update, delete

def home(request):
    return render(request, 'home.html')