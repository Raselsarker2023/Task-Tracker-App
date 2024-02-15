from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.ProjectModelAPIView)
from . import views
urlpatterns = [
    path('', include(router.urls)),
]


# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from . import views
# urlpatterns = [
#     path('', views.ProjectModelAPIView.as_view(), name='project_list'),
# ]