from django.conf import settings
import openai
import logging

class OpenAIService:
    def __init__(self, api_key=settings.OPENAI_API_KEY):
        self.api_key = api_key

    def generate_chat_response(self, messages, context=None):
        try:
            if context:
                for message in messages:
                    if "role" in message and message["role"] == "system":
                        message["content"] = self.update_system_message(message["content"], context)

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=messages,
                max_tokens=settings.DEFAULT_SETTINGS["max_tokens"],
                temperature=settings.DEFAULT_SETTINGS["temperature"],
            )
            model_response = response["choices"][0]["message"]["content"]
            return model_response
        except openai.error.OpenAIError as e:
            logging.exception(f"OpenAI API error: {e}")
            raise OpenAIError(f"OpenAI API error: {e}") from e
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            raise

    def update_system_message(self, system_message, context):
        if "user_goals" in context:
            goals = ", ".join(context["user_goals"])
            system_message = system_message.replace("{user_goals}", goals)

        return system_message
