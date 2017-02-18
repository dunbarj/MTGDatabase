from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.getIndex, name='GetIndex'),
]