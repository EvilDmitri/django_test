from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),

    # ex: /polls/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #
    # ex: /polls/5/results/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

    # ex: /polls/create/
    url(r'^create/$', views.create, name='create'),

    # ex: /polls/delete/1
    url(r'^delete/(?P<poll_id>\d+)$', views.delete, name='delete'),
)