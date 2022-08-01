from django.contrib import admin
from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'deadline', 'status', 'priority', 'importance', 'user']
    search_fields = ['name', 'text', 'deadline', 'status', 'priority', 'importance']
    list_filter = ['name', 'text', 'deadline', 'status', 'priority', 'importance', 'user']
    list_editable = ['name', 'text', 'deadline', 'status', 'priority', 'importance', 'user']

    class Meta:
        model = Task


admin.site.register(Task, TaskAdmin)
