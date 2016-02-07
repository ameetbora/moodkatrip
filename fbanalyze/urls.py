from django.conf.urls import patterns, url
from fbanalyze import views

urlpatterns = patterns('',
                   url(r'^$', views.index, name = 'index'),
		   		   
                       
)
	