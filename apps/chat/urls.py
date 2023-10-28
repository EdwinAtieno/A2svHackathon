from django.urls import path
from .api_views import ChatSessionListCreateView, ChatMessageListCreateView

urlpatterns = [
    path('chat-sessions/', ChatSessionListCreateView.as_view(), name='chat-session-list-create'),
    path('chat-messages/', ChatMessageListCreateView.as_view(), name='chat-message-list-create'),
]
