from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.filters import SearchFilter


# Create your views here.

class TaskModelViewset(viewsets.ModelViewSet):
    queryset = models.TaskModel.objects.all()
    serializer_class = serializers.TaskModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'priority', 'status', 'Cancel_reason']
    
    
class ManagerViewset(viewsets.ModelViewSet):
    queryset = models.Manager.objects.all()
    serializer_class = serializers.ManagerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'email', 'phone_no']
    
    
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'email', 'phone_no']
    
    
class EmployeeAssignViewset(viewsets.ModelViewSet):
    queryset = models.EmployeeAssign.objects.all()
    serializer_class = serializers.EmployeeAssignSerializer
    filter_backends = [SearchFilter]
    search_fields = ['assigned_date']
    
   
   
   
   
   
   
    

# class UpdateTaskAPI(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def put(self, request, id, format=None):
#         task = self.get_object(id)
#         serializer = TaskModelSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get_object(self, id):
#         queryset = TaskModel.objects.all()
#         return get_object_or_404(queryset, pk=id)


# class DeleteTaskAPI(APIView):
#     def delete(self, request, id, format=None):
#         task = get_object_or_404(TaskModel, pk=id)
#         task.delete()
#         return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# class TaskModelAPIView(APIView):
#     def get(self, request, pk=None):
#         if pk is not None:
#             task = TaskModel.objects.get(pk=pk)
#             serializer = TaskModelSerializer(task)
#             return Response(serializer.data)
#         else:
#             tasks = TaskModel.objects.all()
#             serializer = TaskModelSerializer(tasks, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = TaskModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None):
#         if pk is not None:
#             task = TaskModel.objects.get(pk=pk)
#             serializer = TaskModelSerializer(task, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'Please provide a valid task ID.'}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None):
#         if pk is not None:
#             task = get_object_or_404(TaskModel, pk=pk)
#             task.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             TaskModel.objects.all().delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)