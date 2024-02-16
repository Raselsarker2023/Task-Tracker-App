from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from .constants import STATUS_CHOICES, PRIORITY_CHOICES

# Create your models here.
    
class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_assigned_to')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    daily_target = models.IntegerField(default=1 , null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    assigned_to = models.ManyToManyField(User, blank=True) 
    Cancel_reason = models.CharField(max_length=10)


    def __str__(self):
        return self.title
    
    
    
class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15) 

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='employees')  # Added related_name
    name = models.CharField(max_length=50)  
    email = models.EmailField()
    phone_no = models.CharField(max_length=15) 

    def __str__(self):
        return self.name

class EmployeeAssign(models.Model):  
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    employee = models.ManyToManyField(Employee, blank=True)
    assigned_date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.employee.name} assigned to {self.task.title} on {self.assigned_date}"
