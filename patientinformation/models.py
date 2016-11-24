from django.db import models

class Patient(models.Model):
 	"""docstring for Patient """
 	first_name = models.CharField(max_length=100,null=True)
 	last_name = models.CharField(max_length=100,null=True)
 	age = models.CharField(max_length=100,null=True)
 	phone = models.CharField(max_length=100,null=True)
 	gender = models.CharField(max_length=100,null=True,default='male')
 	dob = models.CharField(max_length=100,null=True)
 	email = models.CharField(max_length=100,null=True)
 	comment = models.TextField(null=True)
 	
 	def __str__(self):
 		return 'Patient: ' + self.first_name +' '+ self.last_name
