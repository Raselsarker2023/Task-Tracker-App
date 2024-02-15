from rest_framework import serializers
from . import models

class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectModel
        fields = '__all__'