import secrets

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import RegisterForm, LoginForm, UserForm, RecoveryForm
from users.models import User
from users.services import make_random_password


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    pass


class UserRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(15)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/confirm-email/{token}/'
        send_mail(
            subject="Верификация почты на сайте Products-Shop",
            message=f"Доброго времени суток! "
                    f"Для подтверждения регистрации на сайте Products-Shop перейдите по ссылки {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordResetView(PasswordResetView):
    form_class = RecoveryForm
    template_name = 'users/recovery_form.html'

    def form_valid(self, form):
        if self.request.method == 'POST':
            user_email = self.request.POST['email']
            user = User.objects.filter(email=user_email).first()
            if user:
                password = make_random_password()
                user.set_password(password)
                user.save()
                try:
                    send_mail(
                        subject="Восстановление пароля на сайте Products-Shop",
                        message=f"Доброго времени суток! "
                                f"Ваш пароль для доступа на сайт Products-Shop изменен:\n"
                                f"Данные для входа:\n"
                                f"Email: {user_email}\n"
                                f"Пароль: {password}",
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[user.email]
                    )
                except Exception:
                    print(f"Ошибка при отправке пароля юзеру: ({user=}), на email: {user_email}")
            return HttpResponseRedirect(reverse('users:login'))
        return super().form_valid(form)
