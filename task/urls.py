from django.urls import path
from task.views import TaskDetailView

urlpatterns = [
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail')
]
