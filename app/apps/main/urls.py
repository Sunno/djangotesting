from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'main.views.other'),
	url(r'^([a-zA-Z]+)$', 'main.views.other')
)
