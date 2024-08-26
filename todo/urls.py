from django.urls import path
from . import views

urlpatterns = [
    #Add Task Feature
    path('addTask/', views.addTask, name='addTask'),
    # the request will go to addTask funtion which is inside views.py
    # Mark as done feature
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # THE above mark_as_done and pk is used when, user clicks on mark_as_done it needs to be moved from todays tasks to completed tasks
    # so it is done using the primary key(pk)
    # Mark as undone feature
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # Edit the task feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # Delete task feature
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task')

]
