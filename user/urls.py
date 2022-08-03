from django.urls import path
from user.views import RegisterFormView, LoginFormView, LogoutView

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
