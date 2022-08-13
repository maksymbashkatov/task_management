from django.contrib import admin
from core.tm_functions import send_email
from task.models import Task
from user.models import CustomUser, Dashboard
from django.contrib.auth.admin import UserAdmin


@admin.action(description='Block selected users')
def block_user(modeladmin, request, queryset):
    queryset.update(is_blocked=True)


@admin.action(description='Unblock selected users')
def unblock_user(modeladmin, request, queryset):
    queryset.update(is_blocked=False)


@admin.action(description='Deactivate selected users')
def cancel_confirm_user(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    change_list_template = 'user/general_statistic.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        t_o = Task.objects

        response.context_data.update({
            'total_users': CustomUser.objects.count(),
            'total_tasks': t_o.count(),
            'todo_tasks': t_o.filter(status='todo').count(),
            'in_progress_tasks': t_o.filter(status='in_progress').count(),
            'blocked_tasks': t_o.filter(status='blocked').count(),
            'finished_tasks': t_o.filter(status='finished').count()
        })

        return response


class TaskInline(admin.TabularInline):
    model = Task
    fields = ('name', 'short_text')
    readonly_fields = ('name', 'short_text')

    def short_text(self, obj):
        return f'{obj.text[:10]}...'


class CustomUserAdmin(UserAdmin):
    inlines = (TaskInline,)
    actions = [block_user, unblock_user, cancel_confirm_user]

    # List of CustomUser model fields
    # ('id', 'email', 'first_name', 'last_name', 'work_position', 'password', 'is_active', 'is_blocked')

    # List of users form
    list_display = ('first_name', 'last_name', 'work_position', 'email', 'total_tasks', 'is_active', 'is_blocked')
    search_fields = ('first_name', 'last_name')

    # User form
    # fields = ('first_name', 'last_name', 'email', 'total_tasks')
    readonly_fields = ('total_tasks',)

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'total_tasks')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'work_position', 'password1', 'password2'),
        }),
    )

    def total_tasks(self, obj):
        return Task.objects.filter(user=obj).count()

    def save_model(self, request, obj, form, change):
        obj.save()
        send_email(obj.email, obj.uuid)

    def has_change_permission(self, request, obj=None):
        return False if obj else True

    class Meta:
        model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
