from django.contrib import admin
from django.urls import path, include
from drf_task.urls import router_tasks
from rest_framework.authtoken import views
from drf_user.urls import router_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('task.urls')),
    path('users/', include('user.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('drf_tasks/', include(router_tasks.urls), name='drf_task_list'),
    path('drf_users/', include(router_users.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
