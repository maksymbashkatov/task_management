from django.urls import path
from task.views import TaskDetailView, TaskListView, TaskStatisticsListView

urlpatterns = [
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('all/', TaskListView.as_view(), name='task_list'),
    path('task_statistics/', TaskStatisticsListView.as_view(), name='task_statistics')
]
