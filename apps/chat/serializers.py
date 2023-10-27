from rest_framework import serializers
from .models import ChatSession, ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = '__all__'

    def create(self, validated_data):
        # Extract 'user' and 'conversation_history' from validated_data
        user = validated_data.pop('user')
        conversation_history = validated_data.pop('conversation_history', [])

        # Create a new instance without 'user' and 'conversation_history'
        instance = ChatSession.objects.create(**validated_data)

        # Set 'user', 'conversation_history', and save the instance
        instance.user = user
        instance.conversation_history = conversation_history
        instance.save()

        return instance