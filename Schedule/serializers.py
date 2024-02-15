from rest_framework import serializers
from . import models

class ScheduleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ScheduleModel
        fields = '__all__'