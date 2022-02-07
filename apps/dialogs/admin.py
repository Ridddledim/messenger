from django.contrib import admin

from .models import Message, Thread


class ThreadAdmin(admin.ModelAdmin):
    fields = ("participants",)
    list_display = ("__str__", "created_at", "updated_at")


class MessageAdmin(admin.ModelAdmin):
    list_display = ("text", "sender", "thread", "created_at", "updated_at")
    list_filter = ("sender", "thread")
    ordering = ("text",)
    search_fields = ("text",)


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Message, MessageAdmin)
