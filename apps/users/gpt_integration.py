import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_customer(
        prompt,
        model="gpt-3.5-turbo-0613",
        max_tokens=None,
        top_p=None,
        frequency_penalty=None,
        presence_penalty=None,
        temperature=None,
    ):
    """
    Chat with the OpenAI GPT-3 model to generate responses based on a given prompt.

    Parameters:
    - prompt (str): The input prompt for the model.
    - model (str): The GPT-3 model to use (default: "gpt-3.5-turbo-0613").
    - max_tokens (int): The maximum number of tokens in the generated response (default: 3000).
    - top_p (float): Top-p nucleus sampling parameter (default: 0.8).
    - frequency_penalty (float): Control for diversity of output (default: 0.5).
    - presence_penalty (float): Control for avoiding repetition (default: 0).
    - temperature (float): Control for randomness and creativity (default: 0.7).

    Returns:
    - str: The generated response from the model.
    """

    max_tokens = max_tokens or 3000
    top_p = top_p or 0.8
    frequency_penalty = frequency_penalty or 0.5
    presence_penalty = presence_penalty or 0
    temperature = temperature or 0.7

# revenue
# competition
# data protection
# financial advice
# localised built apps according to kenya requirements
# fraud protection
# incorporate file upload e.g bank statements for information extraction
# financial modelling functionality
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful financial advisor. \
                        You are skilled in financial matters and risk assessment to offer financial advise. \
                        Analize the shared customer data to generate recommendations for the customer \
                        Also recommend a healthier financial life and products like real estate, bonds, and stocks based on the customer risk tolerance." \
                },
                {
                    "role": "user", 
                    "content": prompt
                },
            ],
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            temperature=temperature,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while processing the request."
