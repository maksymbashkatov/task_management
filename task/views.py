from django.shortcuts import render
from django.views.generic import DetailView
from task.models import Task


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'
