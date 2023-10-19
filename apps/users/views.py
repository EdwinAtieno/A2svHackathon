from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .gpt_integration import chat_with_customer
from .recommendation_logic import recommend_products
import uuid
from rest_framework.exceptions import ValidationError

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
        # Check if the provided ID is a valid uuid
        try:
            customer_uuid = uuid(customer_id)
        except ValueError:
            raise ValidationError("Invalid customer ID format")

        # Retrieve the customer using the uuid
        customer = get_object_or_404(User, id=customer_uuid)
        serializer = UserSerializer(customer)

        prompt = f"Customer with ID {customer_id}: {serializer.data}"

        # GPT-3
        try:
            response = chat_with_customer(prompt)
        except GPT3Error as e:
            return Response({'error': f'GPT-3 API error: {str(e)}'}, status=500)

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
            dependants=customer.dependants,
            loan=customer.loan,
            default=customer.default,
            mortgage_balance=customer.mortgage_balance,
            spending_pattern=customer.spending_pattern,
            age=customer.age,
            marital_status=customer.marital_status,
        )

        # GPT-3 response and recommendation
        combined_response = f"{response}\n\nBased on your banking data, here's a recommendation: {recommendation}"

        return Response({'combined_response': combined_response})
    except User.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=404)
    except ValidationError as e:
        return Response({'error': str(e)}, status=400)