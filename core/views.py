from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Cage
from datetime import datetime
import numpy as np
import math
import os

# Create your views here.
from .forms import createForm
def home(request):
	return render(request,'home.html')
	
def create(request):
	form = createForm(request.POST or None)
	if form.is_valid() :
		form.save()
		form = createForm()
	return render(request, "create.html",{'form': form})

# def cage_detail_view(request):
# 	for i in Cage.objects.all():
# 		str1=str(i.stop_time)
# 		str2=str(i.start_time)
# 		str1=str1[0:len(str1)-6]
# 		str2=str2[0:len(str2)-6]
# 		a=datetime.strptime(str1, '%Y-%m-%d %H:%M:%S')
# 		b=datetime.strptime(str2, '%Y-%m-%d %H:%M:%S')
# 		i.diff=str(a-b)
# 		i.save()
# 	obj= Cage.objects.all().values('name','station','diff').distinct()
# 	return render(request,"detail.html",{'Cages':obj})

def new(request):
	for i in Cage.objects.all():
		str1=str(i.stop_time)
		str2=str(i.start_time)
		str1=str1[0:len(str1)-6]
		str2=str2[0:len(str2)-6]
		a=datetime.strptime(str1, '%Y-%m-%d %H:%M:%S')
		b=datetime.strptime(str2, '%Y-%m-%d %H:%M:%S')
		i.diff=str(a-b)
		i.save()
	l=Cage.objects.all().values('name').distinct()
	result={}
	for i in l:
		str1=str(i['name'])
		result[str1]={'1':None,'2':None,'3':None}
	print(result)
	for k in Cage.objects.all():
		strp=str(k.name)
		result[strp][str(k.station)]=k.diff
		# if(k.station==1):
		# 	result[strp]['St1']=k.diff
		# elif(k.station==2):
		# 	result[strp]['St2']=k.diff
		# elif(k.station==3):
		# 	result[strp]['St3']=k.diff

	print(result)
	return render(request,"detail.html",{'Cages':result})

	