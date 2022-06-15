from unicodedata import name
from django.urls import path

from .views import ( home, 
addarticle, 
takearticledetails,
articleslist, 
takearticle, 
takelist,
takedetails,
addfourni,
fournilist,
feedarticle,
notAuto )



urlpatterns = [
	path('', home, name='home'),

	# Articles Routes
	path('addarticle', addarticle, name='addarticle'),
	path('articleslist', articleslist, name='articleslist'),

	# Take Articles Routes
	path('takearticle', takearticle, name='takearticle'),
	path('takelist', takelist, name='takelist'),
	path('takedetails/<int:id>/', takedetails, name='takedetails'),
	path('takearticledetails/<int:id>/', takearticledetails, name='takearticledetails'),

	# Feed Articles Routes
	path('feedarticle', feedarticle, name='feedarticle'),

	#Add Founi
	path('addfourni', addfourni, name='addfourni'),
	path('fournilist', fournilist, name='fournilist'),

	#Not Autho
	path('not_autho', notAuto, name="not_autho")
]