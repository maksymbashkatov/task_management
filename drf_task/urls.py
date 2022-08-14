from django.urls import path
from rest_framework import routers
from drf_task.views import TaskViewSet

router_tasks = routers.SimpleRouter()
router_tasks.register('all', TaskViewSet, basename='drf_all')
