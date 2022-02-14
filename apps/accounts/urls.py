from django.urls import path

from apps.accounts.views import LoginUser, PasswordChangingView, RegisterUser

urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("change_password/<str:token>/", PasswordChangingView.as_view(), name="password"),
]
