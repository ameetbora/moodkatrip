from django.conf.urls import patterns, include, url
from django.contrib import admin
from fbanalyze.api import MoodResource

mood_resource = MoodResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moodkatrip.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(mood_resource.urls)),
    url(r'^fbanalyze/', include('fbanalyze.urls')),
)
