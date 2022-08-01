from django.contrib import admin
from user.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'work_position', 'password', 'is_active']
    search_fields = ['email', 'first_name', 'last_name', 'work_position', 'is_active']
    list_filter = ['first_name', 'last_name', 'work_position', 'is_active']
    list_editable = ['first_name', 'last_name', 'work_position', 'password', 'is_active']

    class Meta:
        model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
