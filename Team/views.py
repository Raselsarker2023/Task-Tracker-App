from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.filters import SearchFilter

# Create your views here.

class TeamModelViewset(viewsets.ModelViewSet):
    queryset = models.TeamModel.objects.all()
    serializer_class = serializers.TeamModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']

    
    
    
    
    
    
    
# class GetTeamAPIView(APIView):
#     def get(self, request, pk=None):
#         if pk is not None:
#             team = TeamModel.objects.get(pk=pk)
#             serializer = TeamModelSerializer(team)
#             return Response(serializer.data)
#         else:
#             teams = TeamModel.objects.all()
#             serializer = TeamModelSerializer(teams, many=True)
#             return Response(serializer.data)
        
# class CreateTeamAPIView(APIView):
#     def post(self, request):
#         serializer = TeamModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UpdateTeamAPIView(APIView):
#     def put(self, request, id, format=None):
#         team = self.get_object(request, id)  # Fix variable name to 'team'
#         serializer = TeamModelSerializer(team, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get_object(self, request, id):
#         queryset = TeamModel.objects.all()
#         return get_object_or_404(queryset, pk=id)


# class DeleteTeamAPIView(APIView):
#     def delete(self, request, pk=None):
#         if pk is not None:
#             team = get_object_or_404(TeamModel, pk=pk)
#             team.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             TeamModel.objects.all().delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)