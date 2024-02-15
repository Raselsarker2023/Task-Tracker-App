from rest_framework import serializers
from . import models


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskModel
        fields = '__all__'
        
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manager
        fields = '__all__'
        
        
class EmployeeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.Employee
        fields = '__all__'
        
        
class EmployeeAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmployeeAssign
        fields = '__all__'