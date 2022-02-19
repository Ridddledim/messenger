from django.db import models

from ..accounts.models import User


class MessageManager(models.Manager):
    def read(self):
        return super().get_queryset().filter(is_read=True)

    def unread(self):
        return super().get_queryset().filter(is_read=False)


class Thread(models.Model):
    participants = models.ManyToManyField(User, related_name="user_thread")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of Thread."""
        return f"Thread {self.id}"


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_sender")
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="message_thread")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    objects = MessageManager()

    def __str__(self):
        """String representation of Message."""
        return self.text
