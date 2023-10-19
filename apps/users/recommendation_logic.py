from datetime import datetime

def recommend_products(
    monthly_income,
    monthly_expenses,
    savings_balance,
    loan_balance,
    credit_card_limit,
    fixed_deposit_balance,
    monthly_deposit,
    mortgage_balance,
    spending_pattern,
):
    chat_records = []

    if monthly_income > monthly_expenses:
        if savings_balance > 0:
            if fixed_deposit_balance and fixed_deposit_balance > 5000:
                recommendation = 'Considering your positive cash flow, you may benefit from maintaining a healthy savings balance and exploring fixed deposit options.'
            else:
                recommendation = 'Given your positive cash flow, consider building an emergency fund and exploring investment options.'
        elif loan_balance > 0:
            recommendation = 'Considering your positive cash flow, it may be a good time to accelerate loan repayments and reduce overall debt.'
    if spending_pattern == 'High':
        recommendation = 'Given your high spending pattern, consider reviewing your budget and exploring high-interest savings accounts to maximize returns.'
    
    if 'recommendation' not in locals():
        recommendation = 'A regular savings account might suit your needs. It\'s essential to regularly review your financial goals and consider diverse options.'

    # Log the recommendation in chat history
    chat_records.append({
        "timestamp": datetime.now().isoformat(),
        "sender": "system",
        "message": recommendation
    })

    additional_info = (
        'Customize recommendations based on specific account types and customer profiles.\n'
        'Provide educational information alongside recommendations.\n'
        'Encourage customers to consult with financial advisors for personalized advice.'
    )

    # Log additional information in chat history
    chat_records.append({
        "timestamp": datetime.now().isoformat(),
        "sender": "system",
        "message": additional_info
    })

    combined_recommendation = f"{recommendation}\n\nAdditional Considerations:\n{additional_info}"

    return combined_recommendation, chat_records
