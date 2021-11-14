from django.db import models

# Create your models here.
class employee(models.Model):
	fname = models.CharField(max_length=10)
	lname = models.CharField(max_length=10)	
	emp_id = models.IntegerField()

	def __str__(self):
		return f"{self.fname} {self.lname}"	