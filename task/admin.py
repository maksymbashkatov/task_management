from django.contrib import admin
from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    # List of Task model fields
    # ('id', 'name', 'text', 'deadline', 'status', 'priority', 'importance', 'user')

    # List of tasks form
    list_display = ('name', 'short_description', 'task_owner')
    search_fields = ('name',)
    list_filter = ('user',)

    # Task form
    fields = ('name', 'text', 'user', 'status')
    readonly_fields = ('user',)

    def short_description(self, obj):
        return obj.text[:30]

    def task_owner(self, obj):
        u = obj.user
        return f'{u.first_name} {u.last_name}'

    class Meta:
        model = Task


admin.site.register(Task, TaskAdmin)
