from django.contrib import admin

from .models import Project, Project_from_task, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'url_git']

@admin.register(Project_from_task)
class ProjecFromTasktAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'url_git']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'url_git']

