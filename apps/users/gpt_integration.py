import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_customer(
        prompt,
        model="text-davinci-003",
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0):

    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while processing the request."
