import json
from django.shortcuts import render
from dajaxice.core import dajaxice_functions


def primer(request, message):
    return_message = u'Received message: {0}'.format(message)
    return json.dumps({'message': return_message})


def index(request):
    return render(request, 'jsrpc/index.html')