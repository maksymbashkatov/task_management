from rest_framework import routers
from drf_user.views import CustomUserViewSet

router_users = routers.SimpleRouter()
router_users.register('user', CustomUserViewSet, basename='drf_user')
