from django.db import models

# Create your models here.

class WaterHole(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	description = models.TextField()
	address = models.CharField(max_length = 100 , blank=True, null=True)
	logo = models.ImageField(upload_to = 'media/logo-waterhole',blank=True, null=True)
	tel_cel_one = models.CharField(max_length = 10, blank=True, null=True)
	tel_cel_two = models.CharField(max_length = 10, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)


	def __str__(self):
		return self.name