from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.accounts.models import User
from apps.dialogs.models import Message, Thread


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
        )


class ThreadSerializer(ModelSerializer):
    participants_details = UserSerializer(many=True, read_only=True, source="participants")

    class Meta:
        model = Thread
        fields = ("id", "participants", "participants_details")

    @staticmethod
    def validate_participants(value):
        if len(value) > 2 or not value:
            raise ValidationError("Must be only 2 participants")
        return value


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ("text", "sender", "thread", "is_read")
