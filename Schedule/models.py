from django.db import models
from django.contrib.auth.models import User
from . constants import STATUS_CHOICES


class ScheduleModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    reminder_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    completed = models.BooleanField(default=False)
    cancel_reason = models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.title
    

