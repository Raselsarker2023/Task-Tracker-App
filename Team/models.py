from django.db import models
from django.contrib.auth.models import User
from projects.models import ProjectModel
from Tasks.models import TaskModel 

class TeamModel(models.Model):
    members = models.ManyToManyField(User, related_name='teams')
    projects = models.ManyToManyField(ProjectModel, related_name='teams')
    tasks = models.ManyToManyField(TaskModel, related_name='teams')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
