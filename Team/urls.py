from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.TeamModelViewset)

urlpatterns = [
    path('', include(router.urls)),
]

# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('', views.TeamModelViewset.as_view({'get': 'list', 'post': 'create'}), name='team_list_create'),
#     path('details/<int:pk>/', views.GetTeamAPIView.as_view(), name='team_detail'),
#     path('create/', views.CreateTeamAPIView.as_view(), name='team_create'),
#     path('update/<int:id>/', views.UpdateTeamAPIView.as_view(), name='team_update'),
#     path('delete/<int:pk>/', views.DeleteTeamAPIView.as_view(), name='team_delete'),
# ]

