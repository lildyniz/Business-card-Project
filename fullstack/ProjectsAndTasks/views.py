from django.shortcuts import render, get_object_or_404

from ProjectsAndTasks.models import Project, Task


def list_of_works(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    return render(request, 
                  "ProjectsAndTasks/list_of_works.html",
                  {"projects":projects,
                   "tasks":tasks,})