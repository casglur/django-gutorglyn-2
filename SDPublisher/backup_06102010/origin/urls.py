from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

    
urlpatterns = patterns('',
    (r'text/', 'origin.views.text'),
    (r'chapter/(?P<chapter>[^/]+)$', 'origin.views.chapter'),
    (r'page/(?P<page>[^/]+)$', 'origin.views.page'),
    (r'www/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'www'}),
                       
    # Example:

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    #Text:
)

#,
#       (r'chapter/(?P<chapter>[^/]+)$', 'origin.views.chapter'),
#        (r'page/(?P<page>[^/]+)$', 'origin.views.page'),
#        (r'www/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'www'})