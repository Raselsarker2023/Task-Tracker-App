from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from Tasks.models import TaskModel
from .constants import STATUS_CHOICES, PRIORITY_CHOICES

class ProjectModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True) 
    tasks = models.ManyToManyField(TaskModel, blank=True, related_name='projects')
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    abandon_reason = models.TextField()
    daily_target = models.IntegerField(default=1)

    def __str__(self):
        return self.name
