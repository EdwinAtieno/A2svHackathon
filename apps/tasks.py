from typing import Any

import requests
from celery import shared_task
from django.conf import settings


@shared_task
def send_sms(phone_number: str, message: str) -> Any:
    """
    Send SMS to the user with the message specified
    and returns a response object.
    """
    url = f"{settings.ONFON_BASE_URL}/v1/sms/SendSMS"
    headers = {
        "Content-Type": "application/json",
        "AccessKey": settings.ONFON_ACCESS_KEY,
    }
    params = {
        "SenderId": settings.ONFON_SENDER_ID,
        "Message": message,
        "MobileNumbers": phone_number,
        "ApiKey": settings.ONFON_API_KEY,
        "ClientId": settings.ONFON_CLIENT_ID,
    }
    response = requests.post(url=url, params=params, headers=headers)
    return response.json()
