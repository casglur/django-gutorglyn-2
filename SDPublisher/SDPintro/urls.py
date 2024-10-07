from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

    
urlpatterns = patterns('',
      #Text:
        (r'text/', 'SDPintro.views.text'),
        (r'www/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'www'}),

)

