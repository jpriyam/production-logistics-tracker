from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('create/',views.create,name='create'),
	#path('cages/',views.cage_detail_view,name='cages'),
	path('cagesnew/',views.new,name='new')
]