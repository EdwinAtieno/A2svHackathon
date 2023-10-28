from django.conf import settings
import openai
import logging


class OpenAIService:
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY

    def generate_chat_response(self, messages):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=messages,
                max_tokens=settings.DEFAULT_SETTINGS["max_tokens"],
                temperature=settings.DEFAULT_SETTINGS["temperature"],
            )
            model_response = response["choices"][0]["message"]["content"]
            return model_response
        except openai.error.OpenAIError as e:
            logging.error(f"OpenAI API error: {e}")
            return None
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            return None