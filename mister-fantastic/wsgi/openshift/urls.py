from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^', include('FrontEnd.urls', namespace='frontend')),
                       url(r'^database/', include('Database.urls', namespace='database')),
                       url(r'^backend/', include('BackEnd.urls', namespace='backend')),
                       url(r'^admin/', include(admin.site.urls)),
)
