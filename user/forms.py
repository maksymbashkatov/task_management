from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser


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
        return user
