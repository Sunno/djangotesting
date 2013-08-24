# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from datetime import date

from main.forms import PersonForm
from main.models import Person

def home(request):
	people = Person.objects.all()
	return render_to_response('home.html', {'people': people},
							  context_instance=RequestContext(request))


def other(request, param=None):
	if request.method != 'POST':
		form = PersonForm()
		return render_to_response('person.html', {'formulario': form},
								  context_instance=RequestContext(request))
	#procesing form
	form = PersonForm(request.POST)
	if not form.is_valid():
		return render_to_response('person.html', {'formulario': form},
								  context_instance=RequestContext(request))
	#valid form
	person = form.save(commit=False)
	person.birdthdate = date(year=1985, month=5, day=14)
	person.save()

	return HttpResponse('Saved! ' + person.name + " " + unicode(person.id))
