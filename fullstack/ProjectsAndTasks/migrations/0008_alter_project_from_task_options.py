# Generated by Django 4.2.2 on 2024-04-20 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsAndTasks', '0007_project_from_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project_from_task',
            options={'ordering': ['id'], 'verbose_name': 'Project_from_task', 'verbose_name_plural': 'Projects_from_tasks'},
        ),
    ]