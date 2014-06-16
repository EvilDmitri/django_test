from django.conf.urls import patterns, url


urlpatterns = patterns('dynamic_models.views',
                       url(r'^$', 'model_list', name='model_list'),
                       url(r'^(?P<model_name>[\w]+)/$', 'get_qs', name='get_qs'),
                       url(r'^(?P<model_name>[\w]+)/create$', 'create', name='create'),
                       url(r'^(?P<model_name>[\w]+)/(?P<id>\d+)$', 'change', name='change'),
                       )
