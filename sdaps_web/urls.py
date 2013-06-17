from django.conf.urls import patterns, include, url

import sdaps_ctl.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sdaps_web.views.home', name='home'),
    # url(r'^sdaps_web/', include('sdaps_web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(sdaps_ctl.views)),

)
