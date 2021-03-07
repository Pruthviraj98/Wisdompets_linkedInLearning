from django.contrib import admin

from .models import Pet #importing pet class instance from models file

#using decorator from admin module- takes model class as arguement and pass it on our pet model 
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
	#register this class to which model is this associated with

	list_distplay=['name', 'species', 'breed', 'age', 'sex']