from django.shortcuts import render
from patientinformation.models import Patient
import json
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response

# Navigate to home page
def home(request):
	template = 'index.html'
	return render(request, template,{})

#  Navigate to form page 
def patientform(request):
	context = ""
	template = 'add.html'
	return render(request, template, {})

# Navigate to the Display page
def displayPage(request):
	template = 'show.html'
	return render(request, template, {})


# Add patient to the database 
def addpatient(request):
	template = 'add.html'
	first_name = request.GET.get('first_name','')
	last_name = request.GET.get('last_name','')
	age = request.GET.get('age','')
	phone= request.GET.get('phone','')
	gender = request.GET.get('gender','')
	dob = request.GET.get('dob','')
	comment = request.GET.get('comment','')
	email = request.GET.get('email','')
	patient_record = Patient(
						first_name = first_name,
						last_name = last_name,
						age = age,
						phone = phone,
						gender = gender,
						comment = comment,
						email = email,
						dob = dob
					)
	print(patient_record)
	patient_record.save()
	return render(request, template, {})

# Get all patient list
def showpatient(request):
	param = dict()
	data = serializers.serialize("json", Patient.objects.all())
	return HttpResponse(data, content_type='application/json')

# method for deleting patient record
def deletepatient(request):
	param = dict()
	pk = request.GET.get('pk','')
	Patient.objects.filter(pk=pk).delete()
	data = serializers.serialize("json", Patient.objects.all())
	return HttpResponse(data, content_type='application/json')
