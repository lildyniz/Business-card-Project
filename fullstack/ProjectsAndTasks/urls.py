from django.urls import path
from . import views

app_name = 'ProjectsAndTasks'

urlpatterns = [
    path('', views.list_of_works, name='list_of_works'),
]