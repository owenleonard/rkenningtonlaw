from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('website.views',
	url(r'^$', 'index'),
	url(r'(?i)areas$', 'areas'),
	url(r'(?i)profile$', 'profile'),
	url(r'(?i)directions$', 'directions'),
	url(r'(?i)contact$', 'contact'),
	url(r'(?i)thanks$', 'thanks'),
)