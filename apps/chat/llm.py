# from typing import Optional, List
# from django.db import models
# from django.utils import timezone
# from apps.users.models import User
# import openai
# import logging
# from dataclasses import dataclass
# from dotenv import load_dotenv
# import os

# load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")

# DEFAULT_SETTINGS = {
#     "max_tokens": 3000,
#     "top_p": 0.8,
#     "frequency_penalty": 0.5,
#     "presence_penalty": 0,
#     "temperature": 0.7,
# }


# @dataclass
# class ChatSession(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     conversation_history = models.JSONField(default=list)
#     created_at = models.DateTimeField(default=timezone.now)

#     def add_message(self, message: str) -> None:
#         """Adds a message to the conversation history."""
#         self.conversation_history.append(message)
#         self.save()

#     def generate_response(self, prompt: str) -> str:
#         """Generates a response to the given prompt using the GPT-3 model."""
#         try:
#             response = chat_with_customer(
#                 prompt,
#                 messages=self.conversation_history,
#             )

#             self.add_message(response)

#             return response
#         except OpenAIError as e:
#             logging.error(f"OpenAI API error: {e}")
#             return "An error occurred while processing the request."
#         except Exception as e:
#             logging.error(f"Unexpected error: {e}")
#             return "An unexpected error occurred while processing the request."

#     def __str__(self) -> str:
#         return f'Chat Session for {self.user}'


# def chat_with_customer(prompt: str, messages: Optional[List[str]] = None) -> str:
#     """Chats with the OpenAI GPT-3 model to generate responses based on a given prompt.

#     Args:
#         prompt (str): The input prompt for the model.
#         messages (Optional[List[str]]): A list of previous messages in the conversation (default: None).

#     Returns:
#         str: The generated response from the model.
#     """
#     messages = messages or []
#     system_message = {
#         "role": "system",
#         "content": "You are a helpful financial advisor. "
#                    "You are skilled in financial matters and risk assessment to offer financial advice. "
#                    "Analyze the shared customer data to generate recommendations for the customer. "
#                    "Also, recommend a healthier financial life and products like real estate, bonds, and stocks based on the customer's risk tolerance."
#     }

#     if not messages:
#         messages.append(system_message)

#     user_message = {"role": "user", "content": prompt}
#     messages.append(user_message)

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo-0613",
#             messages=messages,
#             max_tokens=DEFAULT_SETTINGS["max_tokens"],
#             top_p=DEFAULT_SETTINGS["top_p"],
#             frequency_penalty=DEFAULT_SETTINGS["frequency_penalty"],
#             presence_penalty=DEFAULT_SETTINGS["presence_penalty"],
#             temperature=DEFAULT_SETTINGS["temperature"],
#         )
#         return response["choices"][0]["message"]["content"].strip()
#     except openai.error.OpenAIError as e:
#         raise OpenAIError(f"An error occurred while processing the request: {e}")
#     except Exception as e:
#         raise OpenAIError(f"An unexpected error occurred while processing the request: {e}")


# def save_chat_session(chat_session: ChatSession) -> None:
#     """Saves the chat session to the database."""
#     try:
#         chat_session.save()
#     except Exception as e:
#         logging.error(f"Database error: {e}")


# def load_chat_session(user_id: str) -> Optional[ChatSession]:
#     """Loads a chat session from the database."""
#     try:
#         chat_session = ChatSession.objects.get(user_id=user_id)
#         return chat_session
#     except ChatSession.DoesNotExist:
#         return None
#     except Exception as e:
#         logging.error(f"Database error: {e}")
#         return None
