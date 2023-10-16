from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .gpt_integration import chat_with_customer
from .recommendation_logic import recommend_products

from .serializers import UserSerializer

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user by admin.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


@api_view(['POST'])
def analyze_customer(request, customer_id):
    try:
        customer = get_object_or_404(User, pk=customer_id)
        serializer = UserSerializer(customer)

        prompt = f"Customer with ID {customer_id}: {serializer.data}"
        response = chat_with_customer(prompt)

        # Recommendation logic
        recommendation = recommend_products(
            account_type=customer.account_type,
            monthly_income=customer.monthly_income,
            monthly_expenses=customer.monthly_expenses,
            savings_balance=customer.savings_balance,
            loan_balance=customer.loan_balance,
            credit_card_limit=customer.credit_card_limit,
            fixed_deposit_balance=customer.fixed_deposit_balance,
            monthly_deposit=customer.monthly_deposit,
            mortgage_balance=customer.mortgage_balance,
            spending_pattern=customer.spending_pattern,
        )

        # GPT-3 response and recommendation
        combined_response = f"{response}\n\nBased on your banking data, here's a recommendation: {recommendation}"

        return Response({'combined_response': combined_response})
    except User.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=404)