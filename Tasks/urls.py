from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('task', views.TaskModelViewset)
router.register('manager', views.ManagerViewset) 
router.register('employee', views.EmployeeViewset) 
router.register('assign', views.EmployeeAssignViewset) 
urlpatterns = [
    path('', include(router.urls)),
]



