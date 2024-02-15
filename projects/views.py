from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters

class ProjectModelAPIView(viewsets.ModelViewSet):
    queryset = models.ProjectModel.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'user__username', 'priority', 'abandon_reason', 'status']

    






# class ProjectModelAPIView(APIView):
#     def get(self, request, pk=None):
#         if pk is not None:
#             project = ProjectModel.objects.get(pk=pk)
#             serializer = ProjectModelSerializer(project)
#             return Response(serializer.data)
#         else:
#             projects = ProjectModel.objects.all()
#             serializer = ProjectModelSerializer(projects, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = ProjectModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None):
#         if pk is not None:
#             project = ProjectModel.objects.get(pk=pk)
#             serializer = ProjectModelSerializer(project, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'Please provide a valid project ID.'}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None):
#         if pk is not None:
#             project = get_object_or_404(ProjectModel, pk=pk)
#             project.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             ProjectModel.objects.all().delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

