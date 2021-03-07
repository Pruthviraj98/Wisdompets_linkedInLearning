from django.shortcuts import render
#HttpRespose class creates the  response objects that views expected to return
from django.http import HttpResponse, Http404
#we can use thi above function instead of the render function because in the case of render functon, it needs template files to execute.

#we need the home view to show up some pets and their details. So import the model of Pet first
from .models import Pet

def home(request):
	pets = Pet.objects.all()#ORM query
	#httpresponse object was previously used to inline a string for an RHTML body
	#this becomes unwieldy if we use large body of html.
	#therefore, large body: Render function.
	#we have to send the objects through the dictonary format to the template.
	return render(request, 'home.html', {'pets':pets,})


def pet_detail(request, pet_id):
	try:
		pet = Pet.objects.get(id=pet_id)
	except Pet.DoesNotExist:
		#return 404 so, import http404
		raise Http404('pet not found')
	return render(request, 'pet_detail.html', {'pet': pet})