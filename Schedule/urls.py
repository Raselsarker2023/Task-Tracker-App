from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.ScheduleModelViewset)

urlpatterns = [
    path('', include(router.urls)),
]




# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from . import views


# urlpatterns = [
#     path('', views.ScheduleModelAPIView.as_view(), name='project_list'),
# ]