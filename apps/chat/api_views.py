from rest_framework import generics, status
from rest_framework.response import Response
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer, ChatMessageSerializer
from apps.chat.chat_service import ChatService
from apps.chat.openai_service import OpenAIService
from django.db import DatabaseError
from openai.error import OpenAIError
import logging

class ChatSessionListCreateView(generics.ListCreateAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def create(self, request, *args, **kwargs):
        try:
            # Validating required field: 'user_message'
            user_message = request.data.get("user_message", "")
            if not user_message:
                return Response({"error": "user_message is required"}, status=status.HTTP_400_BAD_REQUEST)

            openai_service = OpenAIService()
            chat_message = ChatService.process_user_message(request.user, user_message, openai_service)

            if chat_message:
                serializer = ChatMessageSerializer(chat_message)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except DatabaseError as e:
            logging.exception(f"Database error: {e}")
            return Response({"error": "Database error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except OpenAIError as e:
            logging.exception(f"OpenAI error: {e}")
            return Response({"error": "OpenAI error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
