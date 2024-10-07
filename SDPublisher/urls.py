from django.conf.urls.defaults import *
from django.http import HttpResponseRedirect


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
     (r'^$',  lambda r : HttpResponseRedirect('gutorglyn/index/')),
#      (r'^weblog/', include('weblog.urls')),
     (r'^SDPintro/', include('SDPintro.urls')),
#      (r'^testme/', include('testme.urls')),       
     (r'^origin/', include('origin.urls')),
     (r'^gutorglyn/', include('gutorglyn.urls')),
     (r'^white/', include('white.urls')),     
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', admin.site.urls),
)
