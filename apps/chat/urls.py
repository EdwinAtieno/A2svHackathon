<<<<<<< HEAD
from django.urls import path
from .api_views import ChatSessionListCreateView, ChatMessageListCreateView

urlpatterns = [
    path('chat-sessions/', ChatSessionListCreateView.as_view(), name='chat-session-list-create'),
    path('chat-messages/', ChatMessageListCreateView.as_view(), name='chat-message-list-create'),
]
=======
from django.urls import path
from .views import ChatMessageListCreateView, ChatMessageDetailView

urlpatterns = [
    path('api/chat-messages/', ChatMessageListCreateView.as_view(), name='chat-message-list'),
    path('api/chat-messages/<int:pk>/', ChatMessageDetailView.as_view(), name='chat-message-detail'),
]
>>>>>>> 75c18a1 (feat profiles)
