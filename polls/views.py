from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from polls.models import Poll, Rooms, Users


# def index(request):
#     latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#     context = {
#         'title': 'List of Polls',
#         'latest_poll_list': latest_poll_list,
#     }
#     return render(request, 'polls/index.html', context)

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {
        'title': 'List of Polls',
        'latest_poll_list': latest_poll_list,
    }
    return render(request, 'polls/index.html', context)

