from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView
from user.forms import CustomUserCreationForm
from user.models import UserUUID, CustomUser


class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('task_list')
    template_name = 'registration/login.html'

    def form_valid(self, form):
        print('XXX', self.request.user)
        self.user = form.get_user()
        login(self.request, self.user)
        if not self.request.user.is_confirmed:
            return render(self.request, 'user/confirm_user.html')
        else:
            return super().form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     if not self.request.user.is_confirmed:
    #         print(self.request.user)
    #         return render(self.request, 'user/confirm_user.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('task_list'))


class ConfirmUserView(View):
    def get(self, request):
        if 'uuid' in request.GET:
            uuid = UserUUID.objects.get(id=request.GET['uuid'])
            user = uuid.user
            CustomUser.objects.filter(id=user.id).update(is_confirmed=True)
        # return render(request, 'user/confirm_user.html')
        return redirect(reverse('login'))


class NotAuthorizedView(View):
    def get(self, request):
        return render(request, 'user/not_authorized.html')
