from django.conf import settings
import openai
import logging
from apps.chat.openai_service import OpenAIService
from .models import ChatSession, ChatMessage

class ChatService:
    @staticmethod
    def process_user_message(user, user_message, openai_service=None):
        if openai_service is None:
            openai_service = OpenAIService()

        try:
            chat_session, created = ChatSession.objects.get_or_create(user=user)
            llm_response = chat_session.generate_response(user_message, openai_service)
            chat_message = ChatMessage.objects.create(
                user=user,
                user_message=user_message,
                model_response=llm_response
            )
            chat_session.add_message(user_message)
            chat_session.add_message(llm_response)
            chat_session.save()
            return chat_message
        except Exception as e:
            logging.error(f"Error in processing user message: {e}")
            return None
