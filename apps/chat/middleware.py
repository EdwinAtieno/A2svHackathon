from .models import ChatSession

class ChatSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated:
            user = request.user
            chat_session = ChatSession.load_chat_session(user_id=user.id)

            if not chat_session:
                chat_session = ChatSession.objects.create(user=user)

            request.chat_session = chat_session

        response = self.get_response(request)
        return response
