from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=55, blank=False)
	roll = models.IntegerField()
	email = models.EmailField(max_length=55)
	address = models.CharField(max_length=55)
	phone = models.CharField(max_length=15)
	parents = models.CharField(max_length=25)
	photo = models.ImageField(upload_to="students/images", default="")

	def __str__(self):
		return self.name