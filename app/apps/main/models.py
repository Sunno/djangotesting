from django.db import models

# Create your models here.

class Person (models.Model):
	name = models.CharField(max_length=256)
	birdthdate = models.DateField()
	updated = models.DateTimeField(auto_now=True)

