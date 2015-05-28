from django.conf.urls import patterns, url


urlpatterns = patterns('Database.views',

     url(r'^$', 'index', name='index'),

)
