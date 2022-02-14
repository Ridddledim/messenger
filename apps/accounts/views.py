from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm


class PasswordChangingView(PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("register")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["token"] = self.kwargs["token"]
        return context


class LoginUser(auth_views.LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse_lazy("register")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")
