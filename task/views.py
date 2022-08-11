from django.shortcuts import render
from django.views.generic import DetailView, ListView
from task.models import Task


class TaskDetailView(DetailView):
    model = Task

    def get(self, request, *args, **kwargs):
        u = request.user
        if u.is_authenticated:
            if u.is_confirmed:
                return super(TaskDetailView, self).get(request)
            else:
                return render(request, 'user/confirm_user.html')
        else:
            return render(request, 'user/not_authorized.html')


class TaskListView(ListView):
    model = Task

    def get_queryset(self):
        user = self.request.user
        if user.is_active:
            return Task.objects.filter(user=user)
        else:
            return super(TaskListView, self).get_queryset()

    def get(self, request, *args, **kwargs):
        u = request.user
        if u.is_authenticated:
            if u.is_confirmed:
                return super(TaskListView, self).get(request)
            else:
                return render(request, 'user/confirm_user.html')
        else:
            return render(request, 'user/not_authorized.html')


class TaskStatisticsListView(ListView):
    model = Task
    template_name = 'task/task_statistics.html'

    def get_context_data(self, **kwargs):
        t_o = Task.objects.filter(user=self.request.user)
        context = super(TaskStatisticsListView, self).get_context_data(**kwargs)
        context['total_tasks'] = t_o.count()
        context['todo_tasks'] = t_o.filter(status='todo').count()
        context['in_progress_tasks'] = t_o.filter(status='in_progress').count()
        context['blocked_tasks'] = t_o.filter(status='blocked').count()
        context['finished_tasks'] = t_o.filter(status='finished').count()
        # context['average_duration_of_tasks'] = t_o.aggregate(Avg('total_time'))
        return context
