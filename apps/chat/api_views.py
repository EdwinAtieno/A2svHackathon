from rest_framework import generics, status
from rest_framework.response import Response
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer, ChatMessageSerializer
from apps.chat.chat_service import OpenAIService, ChatService
import logging

class ChatSessionListCreateView(generics.ListCreateAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def create(self, request, *args, **kwargs):
        user_message = request.data.get("user_message", "")
        try:
            openai_service = OpenAIService()
            chat_message = ChatService.process_user_message(request.user, user_message, openai_service)
            if chat_message:
                serializer = ChatMessageSerializer(chat_message)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
