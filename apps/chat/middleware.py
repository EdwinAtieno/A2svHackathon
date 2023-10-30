from django.contrib.sessions.models import Session
from django.utils import timezone

class ChatSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', None)

        if user and user.is_authenticated:
            # Assuming you have a `last_activity` field in your ChatSession model
            user_sessions = ChatSession.objects.filter(user=user, last_activity__gte=timezone.now() - timezone.timedelta(days=1)).order_by('-created_at')

            if user_sessions.exists():
                chat_session = user_sessions.first()
            else:
                chat_session = ChatSession.objects.create(user=user)

            request.chat_session = chat_session

        response = self.get_response(request)
        return response
