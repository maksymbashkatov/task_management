from django.urls import path
from task.views import TaskDetailView, TaskListView

urlpatterns = [
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('all/', TaskListView.as_view(), name='task_list')
]
