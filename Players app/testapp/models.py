from django.db import models

# Create your models here.
class Player(models.Model):
	jersyno = models.IntegerField()
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	iplteam = models.CharField(max_length=50)

