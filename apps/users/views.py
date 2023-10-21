import logging
# from .recommendation_logic import recommend_products
import uuid
from datetime import datetime
from django.http import HttpResponse

from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .gpt_integration import chat_with_customer
from .serializers import UserSerializer

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

def analyze_customer(request, customer_id):
    try:
        customer = request.user
        serializer = UserSerializer(customer)

        prompt = f"Customer with ID {customer.id}: {serializer.data}"

        try:
            response = chat_with_customer(prompt)
        except GPT3Error as e:
            return Response({'error': f'GPT-3 API error: {str(e)}'}, status=500)

        try:
            chat_records = generate_recommendation_and_log(customer)
        except Exception as e:
            logging.error(f'Error generating recommendations: {str(e)}')
            return Response({'error': f'Error generating recommendations. Please check the logs for details.'}, status=500)

        combined_response = f"{response}\n\nBased on your banking data, here's a recommendation: {chat_records['recommendation']}"
        http_response = HttpResponse(combined_response)

        http_response.set_cookie('user_id', str(customer.id))

        return Response({
            'response': response,
            'recommendation': chat_records['recommendation'],
            'combined_response': combined_response,
            'chat_records': chat_records['chat_records'],
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@csrf_exempt
def generate_recommendation_and_log(customer):
    chat_records = []
    try:
        prompt = f"Analyzing customer data: {customer}"
        recommendation = chat_with_customer(prompt)

        chat_records.append({
            "timestamp": datetime.now().isoformat(),
            "sender": "system",
            "message": recommendation
        })

        additional_info = (
            'Customize recommendations based on specific account types and customer profiles.\n'
            'Provide educational information alongside recommendations.\n'
            'Give the customer additional investment options based on their financial behavior.\n'
        )

        chat_records.append({
            "timestamp": datetime.now().isoformat(),
            "sender": "system",
            "message": additional_info
        })

        combined_recommendation = f"{recommendation}\n\nAdditional Considerations:\n{additional_info}"

        return {'recommendation': combined_recommendation, 'chat_records': chat_records}
    except Exception as e:
        return {'error': str(e)}


#  increasing savings
#  consolidating loans
#  adjusting spending patterns
#  exploring specific financial products based on the customer's financial health and goals. 