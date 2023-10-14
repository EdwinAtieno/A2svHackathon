from django.contrib import admin
from .models import ChatMessage

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'user_message', 'model_response')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__email', 'user_message', 'model_response')
    list_display_links = ('timestamp',)

    def timestamp_display(self, obj):
        return obj.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    timestamp_display.short_description = 'Timestamp'

admin.site.register(ChatMessage, ChatMessageAdmin)
