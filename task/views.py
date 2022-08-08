from django.shortcuts import render
from django.views.generic import DetailView, ListView
from task.models import Task


class TaskDetailView(DetailView):
    model = Task

    def get(self, request, *args, **kwargs):
        u = request.user
        if u.is_authenticated:
            return render(request, 'task/task_detail.html' if u.is_confirmed else 'user/confirm_user.html')
        else:
            return render(request, 'user/not_authorized.html')


class TaskListView(ListView):
    model = Task

    def get(self, request, *args, **kwargs):
        u = request.user
        if u.is_authenticated:
            return render(request, 'task/task_list.html' if u.is_confirmed else 'user/confirm_user.html')
        else:
            return render(request, 'user/not_authorized.html')
