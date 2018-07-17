from django.db import models
from django.db import models
from django.utils import timezone


class HomePage(models.Model):
	welcome_header = models.CharField(max_length=50)
	welcome_text = models.TextField(max_length=1500)
	supply_header = models.CharField(max_length=50)
	supply_text = models.TextField(max_length=1500)
	our_service_header = models.CharField(max_length=50)
	our_service_text = models.TextField(max_length=1500)


	def __str__(self):
		self.welcome_header

# Create your models here.
