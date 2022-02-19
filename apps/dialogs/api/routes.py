from django.urls import path

from .views import (
    ThreadDetailAPIView,
    ThreadListAPIView,
    UserExitAPIView,
    message_detail,
    message_list,
    message_mark,
)

urlpatterns = [
    path("threads/", ThreadListAPIView.as_view()),
    path("threads/<int:pk>/", ThreadDetailAPIView.as_view()),
    path("threads/<int:pk>/user_exit/<int:user_pk>", UserExitAPIView.as_view()),
    path("threads/<int:pk>/messages", message_list),
    path("threads/messages/<int:message_pk>", message_detail),
    path("threads/messages/mark/<int:message_pk>", message_mark),
]
