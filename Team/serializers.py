from rest_framework import serializers
from . import models

class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamModel
        fields = '__all__'