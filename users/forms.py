from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordResetForm

from catalog.forms import StyleFormMixin
from users.models import User


class LoginForm(StyleFormMixin, AuthenticationForm):
    pass


class RegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'country', 'avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class RecoveryForm(StyleFormMixin, PasswordResetForm):
    pass
