from django.shortcuts import render
from django.views.generic import DetailView, ListView
from task.models import Task


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'


class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
