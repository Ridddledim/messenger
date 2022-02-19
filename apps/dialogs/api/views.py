from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from apps.accounts.models import User
from apps.dialogs.api.serializers import MessageSerializer, ThreadSerializer
from apps.dialogs.models import Message, Thread


class ThreadListAPIView(ListCreateAPIView):
    queryset = Thread.objects.all().prefetch_related("participants")
    serializer_class = ThreadSerializer


class ThreadDetailAPIView(RetrieveAPIView):
    queryset = Thread.objects.all().prefetch_related("participants")
    serializer_class = ThreadSerializer


class UserExitAPIView(GenericAPIView):
    queryset = Thread.objects.all().prefetch_related("participants")
    serializer_class = ThreadSerializer

    def patch(self, request, pk, user_pk):
        thread = Thread.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=user_pk).first()
        if not (thread and user):
            raise Http404
        thread.participants.remove(user)
        thread.save()
        if not thread.participants.all():
            thread.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        serializer = self.get_serializer(thread, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def message_list(request, *args, **kwargs):
    """Returns the response with the list of threads and create a new thread when post"""
    if request.method == "GET":
        thread = Thread.objects.filter(pk=kwargs.get("pk")).first()
        if not thread:
            raise Http404
        messages = Message.objects.filter(thread=thread)
        return Response(data=MessageSerializer(messages, many=True).data, status=HTTP_200_OK)
    request.data["thread"] = kwargs.get("pk")
    serializer = MessageSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=HTTP_201_CREATED)


@api_view(["PATCH", "DELETE"])
def message_detail(request, *args, **kwargs):
    """A view to delete messages and change text of a message"""
    message_pk = kwargs.get("message_pk")
    message = Message.objects.filter(pk=message_pk).first()
    if not message:
        raise Http404
    if request.method == "DELETE":
        message.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    text_changing_data = {"text": request.data.get("text")}
    serializer = MessageSerializer(data=text_changing_data, instance=message, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data)


@api_view(["PATCH"])
def message_mark(request, *args, **kwargs):
    """A view to mark messages as read"""
    message_pk = kwargs.get("message_pk")
    message = Message.objects.filter(pk=message_pk).first()
    if not message:
        raise Http404
    marking_as_read_data = {"is_read": True}
    serializer = MessageSerializer(data=marking_as_read_data, instance=message, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data)
