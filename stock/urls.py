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
addFeedArticles,
feedList,
generate_pdf,
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
	path('feedarticlesdetails/<int:id>/', addFeedArticles, name='feedarticlesdetails'),
	path('feedlist', feedList, name='feedlist'),
	path('generatebr/<int:id>/', generate_pdf, name='generatebr'),

	#Add Founi
	path('addfourni', addfourni, name='addfourni'),
	path('fournilist', fournilist, name='fournilist'),

	#Not Autho
	path('not_autho', notAuto, name="not_autho")
]