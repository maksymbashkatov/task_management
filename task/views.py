from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from task.models import Task


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    login_url = 'not_authorized'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    login_url = 'not_authorized'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskStatisticsListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task_statistics.html'
    login_url = 'not_authorized'

    def get_context_data(self, **kwargs):
        t_o = Task.objects.filter(user=self.request.user)
        context = {
            'total_tasks': t_o.count(),
            'todo_tasks': t_o.filter(status='todo').count(),
            'in_progress_tasks': t_o.filter(status='in_progress').count(),
            'blocked_tasks': t_o.filter(status='blocked').count(),
            'finished_tasks': t_o.filter(status='finished').count()
        }
        # context['average_duration_of_tasks'] = t_o.aggregate(Avg('total_time'))
        return context
