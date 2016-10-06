from django.conf.urls import patterns, include, url
from core import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leafpoints.views.home', name='home'),
    # url(r'^leafpoints/', include('leafpoints.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^leafs/$', views.leafs, name='leafs'),
    url(r'^shadowing/$', views.shadowing, name='shadowing'),
    url(r'^redeem/$', views.redeem, name='redeem'),

)
