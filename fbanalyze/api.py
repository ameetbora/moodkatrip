from tastypie.resources import ModelResource, Resource
from fbanalyze.mood_calculate import mood_calculate
from fbanalyze.models import Places

class MoodResource(ModelResource):
	class Meta:
		queryset = Places.objects.all()
		resource_name = 'mood'
		fields = ['name','type']

	
    	