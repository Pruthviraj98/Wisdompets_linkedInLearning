from django.db import models

class Pet(models.Model):
	SEX_CHOICES=[('M', 'Male'), ('F', 'Female')]#to set choices
	name=models.CharField(max_length=100)
	submitter=models.CharField(max_length=100)
	species=models.CharField(max_length=30)
	breed=models.CharField(max_length=30)
	name=models.CharField(max_length=30, blank=True)#as some dont have names
	description=models.TextField()
	sex=models.CharField(max_length=1, blank=True, choices=SEX_CHOICES)
	submission_date=models.DateTimeField()
	age=models.IntegerField(null=True)
	vaccinations=models.ManyToManyField('Vaccine', blank=True) 
	#since a pet can have many vaccine and a vaccine can be put into many pets,
	#this is a ManyToMany Relationship hence using ManyToMany Field
	#params: 1. Name of the model related to. 2.blank cuz some pets might not have vaccines

#model for tracking vaccine
class Vaccine(models.Model):
	name=models.CharField(max_length=50)

	#for admin to get vaccination names visible
	def __str__(self):
		#tells what string representation should be for this model
		return self.name 