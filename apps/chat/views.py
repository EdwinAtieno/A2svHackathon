from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .sub import run_llama_model


@csrf_exempt
def chat_with_llama(request):
    if request.method == 'POST':
        try:
            input_text = request.POST.get('input_text')

            response = run_llama_model(input_text)

            response_data = {
                'response': response
            }

            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
