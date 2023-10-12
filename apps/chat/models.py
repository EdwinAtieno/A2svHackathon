from django.db import models
from apps.users.models import User


class ChatMessage(models.Model):
    """Stores user chat history"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_message = models.TextField()  # user's quz - outgoing
    model_response = models.TextField()  # Model's response - incoming

    def __str__(self):
        return f'{self.user}: {self.user_message}'
