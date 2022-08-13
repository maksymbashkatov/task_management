from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView, UpdateView
from user.forms import CustomUserCreationForm
from user.models import CustomUser
from django.contrib import messages


class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        messages.success(self.request, 'Test.')
        form.save()
        return super().form_valid(form)


class LoginFormView(LoginView):
    next_page = reverse_lazy('task_list')

    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.get(email=request.POST['username'])
        if user.is_active:
            if user.is_blocked:
                return render(self.request, 'user/blocked_user.html')
            else:
                login(self.request, user)
                return super(LoginFormView, self).post(request)
        else:
            return render(self.request, 'user/confirm_user.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('task_list'))


class ConfirmUserView(View):
    def get(self, request):
        if 'uuid' in request.GET:
            uuid = request.GET['uuid']
            user = CustomUser.objects.filter(uuid=uuid)
            user.update(is_active=True)
        return redirect(reverse('login'))


class NotAuthorizedView(View):
    def get(self, request):
        return render(request, 'user/not_authorized.html')


class CustomUserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'work_position']
    template_name = 'user/profile_page.html'
    login_url = 'not_authorized'

    def get(self, request, *args, **kwargs):
        if self.get_object() == request.user:
            return super(CustomUserUpdateView, self).get(request)
        else:
            return HttpResponseNotFound("You can't edit not you page.")
