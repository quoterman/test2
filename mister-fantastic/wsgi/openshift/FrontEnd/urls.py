from django.conf.urls import patterns, url


urlpatterns = patterns('FrontEnd.views',

     url(r'^$', 'index', name='index'),

)
