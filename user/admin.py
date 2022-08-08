from django.contrib import admin
from user.forms import CustomUserCreationForm
from user.models import CustomUser, UserUUID


class CustomUserAdmin(admin.ModelAdmin):
    add_form_template = CustomUserCreationForm
    list_display = ['id', 'email', 'first_name', 'last_name', 'work_position', 'password', 'is_active', 'is_confirmed']
    search_fields = ['email', 'first_name', 'last_name', 'work_position', 'is_active']
    list_filter = ['first_name', 'last_name', 'work_position', 'is_active']
    list_editable = ['first_name', 'last_name', 'work_position', 'password', 'is_active', 'is_confirmed']

    class Meta:
        model = CustomUser


class UserUUIDAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

    class Meta:
        model = UserUUID


admin.site.register(UserUUID, UserUUIDAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
