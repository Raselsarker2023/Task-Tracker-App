from django.db import models
from django.contrib.auth.models import User
from Schedule.models import ScheduleModel
from projects.models import ProjectModel

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE) 
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    schedules = models.ManyToManyField(ScheduleModel, related_name='user_accounts', blank=True)
    projects = models.ManyToManyField(ProjectModel, related_name='user_accounts', blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


    
