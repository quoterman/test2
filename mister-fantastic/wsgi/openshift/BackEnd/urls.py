from django.conf.urls import patterns, url


urlpatterns = patterns('BackEnd.views',

                       url(r'^$', 'index', name='index'),
                       url(r'home', 'download_repo', name='download_repo')
)
