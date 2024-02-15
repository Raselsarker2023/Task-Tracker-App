
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.filters import SearchFilter

# Create your views here.

class ScheduleModelViewset(viewsets.ModelViewSet):
    queryset = models.ScheduleModel.objects.all()
    serializer_class = serializers.ScheduleModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'status', 'cancel_reason']
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from .models import ScheduleModel
# from .serializers import ScheduleModelSerializer

# # Create your views here.

# class ScheduleModelAPIView(APIView):
#     def get(self, request, pk=None):
#         if pk is not None:
#             schedule = ScheduleModel.objects.get(pk=pk)
#             serializer = ScheduleModelSerializer(schedule)
#             return Response(serializer.data)
#         else:
#             schedules = ScheduleModel.objects.all()
#             serializer = ScheduleModelSerializer(schedules, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = ScheduleModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None):
#         if pk is not None:
#             schedule = ScheduleModel.objects.get(pk=pk)
#             serializer = ScheduleModelSerializer(schedule, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'Please provide a valid project ID.'}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None):
#         if pk is not None:
#             schedule = get_object_or_404(ScheduleModel, pk=pk)
#             schedule.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             ScheduleModel.objects.all().delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)





