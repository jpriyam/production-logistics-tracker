from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import timedelta
from datetime import datetime


# Create your models here.

Stations = (
    (1,'Station A'),
    (2, 'Station B'),
    (3,'Station C'),
)
class Cage(models.Model):

	class Meta:
		unique_together = ('name','station')

	# def timee(t1,t2):
	# 	datetime.strftime(time_str1,'%H:%M')
    
	name = models.CharField(max_length=30,null=False)
	station = models.PositiveSmallIntegerField(choices =Stations)
	start_time = models.DateTimeField() 
	stop_time= models.DateTimeField() 
	diff = models.CharField(max_length=100,default="To be updated")

# class Cage2(models.Model):

# 	name = models.CharField(max_length=30,null=True)
# 	station1 = models.CharField(max_length=100,default="To be updated")
# 	station2 = models.CharField(max_length=100,default="To be updated")
# 	station3 = models.CharField(max_length=100,default="To be updated")
	


