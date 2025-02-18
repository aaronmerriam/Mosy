from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mosy.views.home', name='home'),
    # url(r'^mosy/', include('mosy.foo.urls')),
    (r'^compare/$', 'mosy.mosaic.views.compare'),
    (r'^$', 'mosy.knn.views.index'),
    (r'^d/(?P<dp_id>[0-9]+)/$', 'mosy.knn.views.datapoint'),
    (r'^t/(?P<tile_id>[0-9]+)/$', 'mosy.mosaic.views.tile'),
    (r'^(?P<lsh_id>[0-9]+)/$', 'mosy.knn.views.detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
