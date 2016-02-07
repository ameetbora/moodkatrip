from django.shortcuts import render
from django.http import HttpResponse
from fbanalyze.mood_calculate import mood_calculate
# Create your views here.
def index(request):
	res= " "
	res = mood_calculate()
	return render(request, 'fbanalyze/index.html',{'results':res})