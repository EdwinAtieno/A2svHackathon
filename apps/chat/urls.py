from django.urls import path
from . import views

urlpatterns = [
    path('chat-with-llama/', views.chat_with_llama, name='chat_with_llama'),
]
