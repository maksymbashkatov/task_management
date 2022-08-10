from django.contrib import admin
from task.models import Task
from user.models import CustomUser, UserUUID


class TaskInline(admin.TabularInline):
    model = Task

    def short_text(self, obj):
        return f'{obj.text[:10]}...'

    fields = ('name', 'short_text')
    readonly_fields = ('short_text',)


class CustomUserAdmin(admin.ModelAdmin):
    inlines = (TaskInline,)

    def total_tasks(self, obj):
        return Task.objects.filter(user=obj).count()

    # List of CustomUser model fields
    # ('id', 'email', 'first_name', 'last_name', 'work_position', 'password', 'is_active', 'is_confirmed')

    # List of users form
    list_display = ('first_name', 'last_name', 'work_position', 'email', 'total_tasks')
    search_fields = ('first_name', 'last_name')

    # User form
    fields = ('first_name', 'last_name', 'email', 'total_tasks')
    readonly_fields = ('total_tasks',)

    def has_change_permission(self, request, obj=None):
        return False

    class Meta:
        model = CustomUser


class UserUUIDAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

    class Meta:
        model = UserUUID


admin.site.register(UserUUID, UserUUIDAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
