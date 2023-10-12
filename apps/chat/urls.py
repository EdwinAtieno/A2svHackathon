from django.urls import path
from .views import ChatMessageListCreateView, ChatMessageDetailView

urlpatterns = [
    path('api/chat-messages/', ChatMessageListCreateView.as_view(), name='chat-message-list'),
    path('api/chat-messages/<int:pk>/', ChatMessageDetailView.as_view(), name='chat-message-detail'),
]
