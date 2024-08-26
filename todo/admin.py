from django.contrib import admin
from .models import Task

# Register your models here.
#In the "http://127.0.0.1:8000/admin/todo/task/" we want the all the tasks to be in table format so that we get better
# understanding to do that we need to overwrite admin functionality to do we need to create a class with "model name + Admin" and pass to inherit the admin module which is ModelAdmin 
# write what ever we want inside that, like how you would like to see the admin interface , example the below reperesents the table which contains the fields.
# also search filter will be added in admin interface.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'created_at')
    search_fields = ('task',)

admin.site.register(Task, TaskAdmin)