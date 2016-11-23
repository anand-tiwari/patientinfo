from django.contrib import admin
from patientinformation.models import Patient

class PatientAdmin(admin.ModelAdmin):
	class Meta:
		model = Patient

admin.site.register(Patient, PatientAdmin)
