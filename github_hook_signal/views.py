from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from signals import github_hook_received


@csrf_exempt
def github_hook(request):
    if request.method == 'POST':
        # Decode the payload
        payload = json.loads(request.body)

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

        return JsonResponse(response)
    else:
        # We only allow the POST method
        return HttpResponseNotAllowed(['POST'])
