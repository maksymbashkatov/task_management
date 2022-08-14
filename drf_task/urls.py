from rest_framework import routers
from drf_task.views import TaskGenericViewSet

router_tasks = routers.SimpleRouter()
router_tasks.register('all', TaskGenericViewSet, basename='drf_all')
