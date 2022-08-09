from django.shortcuts import render
from django.views.generic import DetailView, ListView
from task.models import Task


def render_check_user(request, template_for_checked_user):
    u = request.user
    if u.is_authenticated:
        return render(request, template_for_checked_user if u.is_confirmed else 'user/confirm_user.html')
    else:
        return render(request, 'user/not_authorized.html')


class TaskDetailView(DetailView):
    model = Task

    def get(self, request, *args, **kwargs):
        return render_check_user(request, 'task/task_detail.html')


class TaskListView(ListView):
    model = Task

    def get(self, request, *args, **kwargs):
        return render_check_user(request, 'task/task_list.html')
