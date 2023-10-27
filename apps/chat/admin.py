from django.contrib import admin
from .models import ChatMessage, ChatSession

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp_display', 'user_message', 'model_response')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__email', 'user_message', 'model_response')
    list_display_links = ('timestamp_display',)

    def timestamp_display(self, obj):
        return obj.timestamp.strftime("%Y-%m-%d %H:%M:%S")

    timestamp_display.short_description = 'Timestamp'
    timestamp_display.admin_order_field = 'timestamp' 

    readonly_fields = ('timestamp_display',)  

    fieldsets = (
        ('Chat Details', {
            'fields': ('user', 'timestamp_display', 'user_message'),
        }),
        ('Model LLM Response', {
            'fields': ('model_response',),
        }),
    )

    def has_add_permission(self, request):
        return False 

class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at_display')
    search_fields = ('user__email', 'created_at')
    list_display_links = ('created_at_display',)
    date_hierarchy = 'created_at'

    def created_at_display(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    created_at_display.short_description = 'Created At'
    created_at_display.admin_order_field = 'created_at'

    readonly_fields = ('user', 'created_at_display')

    fieldsets = (
        ('Chat Session Details', {
            'fields': ('user', 'created_at_display'),
        }),
    )

    def has_add_permission(self, request):
        return False

admin.site.register(ChatMessage, ChatMessageAdmin)
admin.site.register(ChatSession, ChatSessionAdmin)
