from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from user.models import CustomUser, UserUUID


def send_email(email, uuid):
    confirm_link = f'{Site.objects.get_current().domain}/users/confirm_user/?uuid={uuid}'
    send_mail(
        'Activation link',
        f'Please follow the activation link below.\n{confirm_link}',
        'maksymbashkatov@ukr.net',
        (f'{email}',)
    )


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'work_position')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.work_position = self.cleaned_data['work_position']
        if commit:
            user.save()
            UserUUID.objects.create(user=CustomUser.objects.get(id=user.id))
            send_email(user.email, UserUUID.objects.get(user=user).id)
        return user
