from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^our_products/$', views.our_products, name='our_products'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^thanks/$', views.thanks, name='thanks'),
	]