# from flask import Flask, request, jsonify
# from gpt_integration import chat_with_customer

# app = Flask(__name__)

# def get_user_input(prompt, default=None, data_type=str):
#     input_prompt = f"{prompt} ({default}): " if default is not None else f"{prompt}: "
#     user_input = input(input_prompt).strip()
#     return data_type(user_input) if user_input else default

# def generate_prompt(user_data):
#     prompt = f"Employment Type: {user_data['employment_type']}\n"
#     prompt += f"Country: {user_data['country']}\n"
#     prompt += f"Age: {user_data['age']}\n"
#     prompt += f"Dependants: {user_data['dependants']}\n"
#     prompt += f"Marital Status: {user_data['marital_status']}\n"

#     prompt += f"Account Type: {user_data['account_type']}\n"
#     prompt += f"Monthly Income: {user_data['monthly_income']}\n"
#     prompt += f"Monthly Expenses: {user_data['monthly_expenses']}\n"
#     prompt += f"Savings Balance: {user_data['savings_balance']}\n"
#     prompt += f"Loan Balance: {user_data['loan_balance']}\n"
#     prompt += f"Credit Card Limit: {user_data['credit_card_limit']}\n"
#     prompt += f"Fixed Deposit Balance: {user_data['fixed_deposit_balance']}\n"
#     prompt += f"Monthly Deposit: {user_data['monthly_deposit']}\n"
#     prompt += f"Mortgage Balance: {user_data['mortgage_balance']}\n"

#     prompt += f"Loan: {user_data['loan']}\n"
#     prompt += f"Default: {user_data['default']}\n"

#     return prompt

# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         # Ask the user for input
#         employment_type = get_user_input("Employment Type")
#         country = get_user_input("Country")
#         age = int(get_user_input("Age", default="30"))
#         dependants = int(get_user_input("Dependants", default="0"))
#         marital_status = get_user_input("Marital Status")

#         # Financial Information
#         account_type = get_user_input("Account Type", default="Savings")
#         monthly_income = float(get_user_input("Monthly Income", default="5000"))
#         monthly_expenses = float(get_user_input("Monthly Expenses", default="3000"))
#         savings_balance = float(get_user_input("Savings Balance", default="10000"))
#         loan_balance = float(get_user_input("Loan Balance", default="0"))
#         credit_card_limit = float(get_user_input("Credit Card Limit", default="0"))
#         fixed_deposit_balance = float(get_user_input("Fixed Deposit Balance", default="0"))
#         monthly_deposit = float(get_user_input("Monthly Deposit", default="0"))
#         mortgage_balance = float(get_user_input("Mortgage Balance", default="0"))

#         # Other Information
#         loan = float(get_user_input("Loan", default="0"))
#         default = input("Default (False): ").lower() == "true"

#         # Prepare user data for GPT
#         user_data = {
#             "employment_type": employment_type,
#             "country": country,
#             "age": age,
#             "dependants": dependants,
#             "marital_status": marital_status,
#             "account_type": account_type,
#             "monthly_income": monthly_income,
#             "monthly_expenses": monthly_expenses,
#             "savings_balance": savings_balance,
#             "loan_balance": loan_balance,
#             "credit_card_limit": credit_card_limit,
#             "fixed_deposit_balance": fixed_deposit_balance,
#             "monthly_deposit": monthly_deposit,
#             "mortgage_balance": mortgage_balance,
#             "loan": loan,
#             "default": default,
#         }

#         # Generate prompt based on user data
#         prompt = generate_prompt(user_data)

#         # Use GPT to generate a response based on user data
#         response = chat_with_customer(prompt)

#         return jsonify({'response': response})

#     except ValueError as ve:
#         return jsonify({'error': f'Invalid input: {str(ve)}'}), 400
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(port=5000)
