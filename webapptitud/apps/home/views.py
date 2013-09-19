from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

def index_view(request):
	return render_to_response('index.html',locals(),context_instance=RequestContext(request))
