from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    url = models.URLField(verbose_name='Url')
    url_git = models.URLField(verbose_name='Url GitHub')
    description = models.TextField(blank=True, verbose_name='Description')
    readme = models.TextField(verbose_name='README.md')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, verbose_name='Image')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name
    
class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    url_git = models.URLField(verbose_name='Url in GitHub')
    description = models.TextField(blank=True, verbose_name='Description')
    readme = models.TextField(verbose_name='README.md')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name
