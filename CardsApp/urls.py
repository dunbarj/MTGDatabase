from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^cards/search$', views.cardSearch, name='CardSearch'),
    url(r'^cards/all$', views.getCards, name='GetCards'),
	url(r'^cards/card$', views.getCard, name='GetCard'),
	url(r'^cards/simple$', views.simple, name='Simple'),
    url(r'^loadDB$', views.loadDB, name="LoadDB"),
]