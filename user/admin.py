from django.contrib import admin
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from task.models import Task
from user.models import CustomUser, UserUUID, Dashboard
from django.contrib.auth.admin import UserAdmin


def send_email(email, uuid):
    confirm_link = f'{Site.objects.get_current().domain}/users/confirm_user/?uuid={uuid}'
    send_mail(
        'Activation link',
        f'Please follow the activation link below.\n{confirm_link}',
        'maksymbashkatov@ukr.net',
        (f'{email}',)
    )


@admin.action(description='Block selected users')
def block_user(modeladmin, request, queryset):
    queryset.update(is_blocked=True)


@admin.action(description='Unblock selected users')
def unblock_user(modeladmin, request, queryset):
    queryset.update(is_blocked=False)


@admin.action(description='Cancel confirm selected users')
def cancel_confirm_user(modeladmin, request, queryset):
    queryset.update(is_confirmed=False)


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    change_list_template = 'user/general_statistic.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)

        response.context_data['total_users'] = CustomUser.objects.count()
        t_o = Task.objects
        response.context_data['total_tasks'] = t_o.count()
        response.context_data['todo_tasks'] = t_o.filter(status='todo').count()
        response.context_data['in_progress_tasks'] = t_o.filter(status='in_progress').count()
        response.context_data['blocked_tasks'] = t_o.filter(status='blocked').count()
        response.context_data['finished_tasks'] = t_o.filter(status='finished').count()
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
    # ('id', 'email', 'first_name', 'last_name', 'work_position', 'password', 'is_active', 'is_confirmed', 'is_blocked')

    # List of users form
    list_display = ('first_name', 'last_name', 'work_position', 'email', 'total_tasks', 'is_blocked')
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
        UserUUID.objects.create(user=CustomUser.objects.get(id=obj.id))
        send_email(obj.email, UserUUID.objects.get(user=obj).id)

    def has_change_permission(self, request, obj=None):
        return False if obj else True

    class Meta:
        model = CustomUser


class UserUUIDAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

    class Meta:
        model = UserUUID


admin.site.register(UserUUID, UserUUIDAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
