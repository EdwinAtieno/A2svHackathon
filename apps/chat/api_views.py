from rest_framework import generics, status
from rest_framework.response import Response
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer, ChatMessageSerializer
import openai
import logging

from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatSessionListCreateView(generics.ListCreateAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer


from rest_framework import generics, status
from rest_framework.response import Response
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer, ChatMessageSerializer
import logging

class ChatSessionListCreateView(generics.ListCreateAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def create(self, request, *args, **kwargs):
        chat_session, created = ChatSession.objects.get_or_create(user=request.user)

        # Get the user_message from the request data
        user_message = request.data.get("user_message", "")

        # Generate response using the ChatSession model method
        llm_response = chat_session.generate_response(user_message)

        # Create a new ChatMessage with the user, user_message, and llm_response
        chat_message = ChatMessage.objects.create(
            user=request.user,
            user_message=user_message,
            model_response=llm_response
        )

        # Add the new message to the chat session
        chat_session.add_message(user_message)
        chat_session.add_message(llm_response)
        chat_session.save()

        # Use the ChatMessageSerializer to serialize the ChatMessage instance
        serializer = ChatMessageSerializer(chat_message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)