import openai

openai.api_key = 'XnjdWziDuWqpdqChMhY3T3BlbkFJ8AwfdQpjd3PZejnhNk2x'

def chat_with_customer(
        prompt,
        model="text-davinci-003", 
        max_tokens=None, 
        top_p=None, 
        frequency_penalty=None, 
        presence_penalty=None, 
        temperature=None,
        ):

    max_tokens = max_tokens or 3000
    top_p = top_p or 1
    frequency_penalty = frequency_penalty or 0.5
    presence_penalty = presence_penalty or 0
    temperature = temperature or 0.7

    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while processing the request."
