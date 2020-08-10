from django.forms import ModelForm
from .models import Cage
from django import forms
class createForm(ModelForm):
	class Meta:
		model = Cage
		fields = ['name','station','start_time','stop_time']