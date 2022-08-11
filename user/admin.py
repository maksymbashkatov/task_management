from django.contrib import admin
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from task.models import Task
from user.models import CustomUser, UserUUID
from django.contrib.auth.admin import UserAdmin


def send_email(email, uuid):
    confirm_link = f'{Site.objects.get_current().domain}/users/confirm_user/?uuid={uuid}'
    send_mail(
        'Activation link',
        f'Please follow the activation link below.\n{confirm_link}',
        'maksymbashkatov@ukr.net',
        (f'{email}',)
    )


class TaskInline(admin.TabularInline):
    model = Task

    def short_text(self, obj):
        return f'{obj.text[:10]}...'

    fields = ('name', 'short_text')
    readonly_fields = ('name', 'short_text')


class CustomUserAdmin(UserAdmin):
    inlines = (TaskInline,)

    def total_tasks(self, obj):
        return Task.objects.filter(user=obj).count()

    def save_model(self, request, obj, form, change):
        obj.save()
        UserUUID.objects.create(user=CustomUser.objects.get(id=obj.id))
        send_email(obj.email, UserUUID.objects.get(user=obj).id)

    # List of CustomUser model fields
    # ('id', 'email', 'first_name', 'last_name', 'work_position', 'password', 'is_active', 'is_confirmed')

    # List of users form
    list_display = ('first_name', 'last_name', 'work_position', 'email', 'total_tasks')
    search_fields = ('first_name', 'last_name')

    # User form
    # fields = ('first_name', 'last_name', 'email', 'total_tasks')
    readonly_fields = ('total_tasks',)

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'total_tasks', 'is_confirmed')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'work_position', 'password1', 'password2'),
        }),
    )

    def has_add_permission(self, request):
        return True

    # def has_change_permission(self, request, obj=None):
    #     return False

    class Meta:
        model = CustomUser


class UserUUIDAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

    class Meta:
        model = UserUUID


admin.site.register(UserUUID, UserUUIDAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
