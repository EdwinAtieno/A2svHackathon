# middleware.py
from .models import ChatSession

class ChatSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated:
            user = request.user
            chat_session, created = ChatSession.objects.get_or_create(user=user)
            if created:
                chat_session.save()

            request.chat_session = chat_session

        response = self.get_response(request)
        return response
