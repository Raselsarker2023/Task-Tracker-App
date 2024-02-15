from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.filters import SearchFilter

# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']