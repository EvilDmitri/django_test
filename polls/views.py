from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Poll, Rooms, Users, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def create(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('polls:index'))
    elif request.method == 'POST':
        question = request.POST.get('question')
        p = Poll.objects.create(question=question, pub_date=timezone.now())
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def delete(request, poll_id):
    p = Poll.objects.get(pk=poll_id)
    p.delete()
    return HttpResponseRedirect(reverse('polls:index'))


def change(request, poll_id):
    question = request.POST.get('question')
    p = Poll.objects.get(pk=poll_id)
    p.question = question
    p.save()

