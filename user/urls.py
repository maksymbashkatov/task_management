from django.urls import path
from user.views import RegisterFormView, LoginFormView, LogoutView, ConfirmUserView, NotAuthorizedView

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('confirm_user/', ConfirmUserView.as_view(), name='confirm_user'),
    path('not_authorized/', NotAuthorizedView.as_view(), name='not_authorized')
]
