from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.management import BaseCommand
from django.urls import reverse


class ChangePasswordCommand(BaseCommand):
    help = "Generate link for password change"

    def add_arguments(self, parser):
        parser.add_argument("email")

    def handle(self, *args, **options):
        """
        Generates password reset link for user with an email specified.
        Returns None if user does not exist
        """
        email = options["email"]
        base_url = "http://127.0.0.1:8000"
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=email)  # type: ignore
        except user_model.DoesNotExist:
            return None
        token = PasswordResetTokenGenerator().make_token(user)
        reset_path = reverse("password", kwargs={"token": token})
        return self.stdout.write(f"{base_url}{reset_path}")
