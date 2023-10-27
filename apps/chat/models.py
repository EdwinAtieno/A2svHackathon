import uuid 
from typing import Optional, List
from django.db import models
from django.utils import timezone
from apps.users.models import User
import openai
import logging
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

DEFAULT_SETTINGS = {
    "max_tokens": 2000,
    "top_p": 0.8,
    "frequency_penalty": 0.5,
    "presence_penalty": 0,
    "temperature": 0.7,
}

class ChatSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    conversation_history = models.JSONField(default=list)
    created_at = models.DateTimeField(default=timezone.now)

    def add_message(self, message: str) -> None:
        """Adds a message to the conversation history."""
        self.conversation_history.append(message)
        self.save()

    def generate_response(self, prompt: str) -> Optional[str]:
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

        # The messages list
        messages = [system_message] + user_messages

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=messages,
                max_tokens=DEFAULT_SETTINGS["max_tokens"],
                temperature=DEFAULT_SETTINGS["temperature"],
            )

            model_response = response["choices"][0]["message"]["content"].strip()
            return model_response

        except openai.error.OpenAIError as e:
            logging.error(f"OpenAI API error: {e}")
            return None

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None

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
            chat_session = cls.objects.get(user_id=user_id)
            return chat_session
        except cls.DoesNotExist:
            return None
        except Exception as e:
            logging.error(f"Database error: {e}")
            return None

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    user_message = models.TextField()  # user's query - outgoing
    model_response = models.TextField(null=True, blank=True)  # Model's response to user -- incoming

    def __str__(self):
        return f'{self.user}: {self.user_message}'

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Chat Message'
        verbose_name_plural = 'Chat Messages'

