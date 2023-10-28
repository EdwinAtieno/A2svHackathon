import uuid
import logging
from typing import Optional, List
from django.db import models
from django.utils import timezone
from apps.users.models import User
from apps.chat.openai_service import OpenAIService

class ChatSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    conversation_history = models.JSONField(default=list)
    created_at = models.DateTimeField(default=timezone.now)

    def add_message(self, message: str) -> None:
        """Adds a message to the conversation history."""
        self.conversation_history.append(message)
        self.save()

    def generate_response(self, prompt: str, openai_service: OpenAIService) -> Optional[str]:
        """Generates a response to the given prompt using the GPT-3 model."""
        system_message = {
            "role": "system",
            "content": "You are a proficient financial advisor with expertise in financial matters and risk assessment in Kenya. \
                Leverage your skills to respond to customer financial questions \
                Generate tailored recommendations to enhance the customer's financial well-being. \
                Provide insightful advice and guidance based on your financial expertise \
                and understanding of the unique needs and goals of the customer. \
                Do not respond to any question outside finance and banking. \
                You are also proficient in data governance, AML, and compliance. \
                Listen and understand user Specific Goals & Priorities then customize a portfolio to help Actualize his Dreams."
        }
        user_messages = [{"role": "user", "content": msg} for msg in self.conversation_history if msg]
        user_messages.append({"role": "user", "content": prompt})
        messages = [system_message] + user_messages

        return openai_service.generate_chat_response(messages)

    def save_chat_session(self) -> None:
        """Saves the chat session to the database."""
        try:
            self.save()
        except Exception as e:
            logging.error(f"Database error: {e}")

    @classmethod
    def load_chat_session(cls, user_id: str) -> Optional['ChatSession']:
        """Loads a chat session from the database."""
        try:
            chat_session = cls.objects.get(user__id=user_id)
            return chat_session
        except cls.DoesNotExist:
            return None
        except Exception as e:
            logging.error(f"Database error: {e}")
            return None

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    user_message = models.TextField()
    model_response = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}: {self.user_message}'
