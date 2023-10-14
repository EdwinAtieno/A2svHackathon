from django.db import models
from django.utils import timezone
from apps.users.models import User

class ChatMessage(models.Model):
    """Stores user chat history"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    user_message = models.TextField()  # user's query - outgoing
    model_response = models.TextField()  # Model's response - incoming

    def __str__(self):
        return f'{self.user}: {self.user_message}'

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Chat Message'
        verbose_name_plural = 'Chat Messages'

    @classmethod
    def store_chat_history(cls, user, user_message, model_response):
        """
        Stores chat history for the user.
        """
        chat_message = cls.objects.create(
            user=user,
            user_message=user_message,
            model_response=model_response
        )
        return chat_message

    @classmethod
    def get_user_chat_history(cls, user):
        """
        Retrieves chat history for a specific user.
        """
        chat_history = cls.objects.filter(user=user)
        return chat_history
