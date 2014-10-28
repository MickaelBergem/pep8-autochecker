from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from signals import github_hook_received


@csrf_exempt
def github_hook(request):
    if request.method == 'POST':
        if 'payload' in request.POST:
            # Decode the payload
            payload = json.loads(request.POST['payload'])

            # Send the signal
            receivers = github_hook_received.send(
                sender='githubhookreceiver',
                repository=payload['repository'],
                payload=payload,
            )

            if not receivers:
                response = {'status': 'success', 'message': 'Ok'}

            for receiver in receivers:
                # TODO
                (receiver, response) = receiver

        else:
            # Payload not found
            response = {'status': 'error', 'message': 'No payload', 'body': request.POST}

        return JsonResponse(response)
    else:
        # We only allow the POST method
        return HttpResponseNotAllowed(['POST'])
