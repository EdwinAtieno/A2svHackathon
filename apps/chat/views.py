<<<<<<< HEAD
# from django.contrib.auth.decorators import login_required
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from .models import ChatSession
# from .serializers import ChatSessionSerializer
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import IsAuthenticated

# @csrf_exempt
# @api_view(['GET', 'POST'])
# @login_required  # Web view requires login
# def chat_web_view(request):
#     try:
#         user_id = request.user.id
#         chat_session, created = ChatSession.objects.get_or_create(user=user_id)

#         if request.method == 'POST':
#             user_message = request.data.get('user_message')
#             chat_session.add_message(user_message)
#             response_text = chat_session.generate_response(user_message)
#             return Response({'response': response_text}, status=status.HTTP_200_OK)

#         serializer = ChatSessionSerializer(chat_session)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['POST'])
# @authentication_classes([IsAuthenticated])  # JWT authentication for API view
# @permission_classes([])  # No specific permissions for now
# def chat_api_view(request):
#     try:
#         user_id = request.user.id
#         chat_session, created = ChatSession.objects.get_or_create(user=user_id)

#         if request.method == 'POST':
#             user_message = request.data.get('user_message')
#             chat_session.add_message(user_message)
#             response_text = chat_session.generate_response(user_message)
#             return Response({'response': response_text}, status=status.HTTP_200_OK)

#         serializer = ChatSessionSerializer(chat_session)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
=======
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ChatMessage
from .serializers import ChatMessageSerializer

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ChatMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated] 
>>>>>>> 75c18a1 (feat profiles)
