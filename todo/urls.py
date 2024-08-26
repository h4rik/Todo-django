from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
]
# the request will go to addTask funtion which is inside views.py