from django.shortcuts import render, get_object_or_404

from ProjectsAndTasks.models import Project, Project_from_task, Task


def list_of_works(request):
    projects = Project.objects.all()
    project_from_task = Project_from_task.objects.all()
    tasks = Task.objects.all()
    return render(request, 
                  "ProjectsAndTasks/list_of_works.html",
                  {"projects":projects,
                   "project_from_task":project_from_task,
                   "tasks":tasks,})