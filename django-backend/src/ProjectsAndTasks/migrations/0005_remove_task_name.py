# Generated by Django 4.2.11 on 2024-04-19 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsAndTasks', '0004_remove_task_image_task_readme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
    ]