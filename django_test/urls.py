from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
import dynamic_models

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('dynamic_models.urls', namespace='dynamic')),

    # url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)
