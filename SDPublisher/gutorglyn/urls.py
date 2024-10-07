from django.conf.urls.defaults import *
from django.http import HttpResponseRedirect

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
    
urlpatterns = patterns('',
    (r'^$',  lambda r : HttpResponseRedirect('index/')),
    (r'about/$', 'gutorglyn.views.aboutProject'),     
    (r'biog/$', 'gutorglyn.views.biog'),
    (r'drwm/$', 'gutorglyn.views.drwmConcert'),
    (r'dropdown-titles-cy', 'gutorglyn.views.titleListCy'), 
    (r'dropdown-titles-en', 'gutorglyn.views.titleListEn'),      
    (r'essays/$', 'gutorglyn.views.essays'),   
    (r'generate-title-dropdown', 'gutorglyn.views.generateTitleDropdown'),
    (r'get-name/$', 'gutorglyn.views.getName'),           
    (r'get-personal-names/$', 'gutorglyn.views.getPersonalNames'),  
    (r'get-place-names/$', 'gutorglyn.views.getPlaceNames'),              
    (r'get-poem', 'gutorglyn.views.getPoem'),         
    (r'guidelines', 'gutorglyn.views.guidelines'),                    
    (r'index', 'gutorglyn.views.index'),  
    (r'lines-raw/(?P<poem>[^/]+)/(?P<lg>[^/]+)$', 'gutorglyn.views.rawLines'),
    (r'lines-range-raw/(?P<poem>[^/]+)/(?P<startline>[^/]+)/(?P<endline>[^/]+)$', 'gutorglyn.views.rawLinesRange'),    
    (r'line-raw/(?P<poem>[^/]+)/(?P<line>[^/]+)$', 'gutorglyn.views.rawLine'),
    (r'list-docs', 'gutorglyn.views.docListDropdown'),    
    (r'manuscripts/$', 'gutorglyn.views.getManuscripts'),
    (r'manuscripts-sources/$', 'gutorglyn.views.getManuscriptsSources'), 
    (r'musical-companions', 'gutorglyn.views.musicalCompanions'),         
    (r'name/$', 'gutorglyn.views.name'), 
    (r'name-full/$', 'gutorglyn.views.nameFull'),    
    (r'new', 'gutorglyn.views.indexNew'),        
    (r'patron/$', 'gutorglyn.views.patrons'),   
    (r'people/$', 'gutorglyn.views.people'),
    #(r'part-raw/(?P<poem>[^/]+)$', 'gutorglyn.views.rawPart'),      
    (r'parts-raw/(?P<poem>[^/]+)$', 'gutorglyn.views.rawParts'),    
    (r'patrons-json/$', 'gutorglyn.views.allPatronsJSON'),          
    (r'patron-xml', 'gutorglyn.views.allPatronsXML'),    
    (r'patron-list', 'gutorglyn.views.allPatrons'),         
    (r'poem/$', 'gutorglyn.views.poem'), 
    (r'poem-raw/(?P<poem>[^/]+)$', 'gutorglyn.views.rawPoem'),
    (r'print-this', 'gutorglyn.views.printThis'),         
    (r'search/$', 'gutorglyn.views.search'),
    (r'search-results-blank/$', 'gutorglyn.views.searchResults'),    
    (r'search-results-v1/$', 'gutorglyn.views.searchResultsGlobal'),
    #(r'search-results-paraphrases/$', 'gutorglyn.views.searchResultsParaphrases'),    
    (r'search-start/$', 'gutorglyn.views.searchStart'),         
    (r'service/$', 'gutorglyn.views.service'),    
    (r'title-list', 'gutorglyn.views.titleList'),
    (r'transcripts/$', 'gutorglyn.views.transcripts'),
    (r'transcript-image/$', 'gutorglyn.views.transcriptImage'),     
    (r'transcriptimages/$', 'gutorglyn.views.transcriptImages'),  
    (r'tuchwith/$', 'gutorglyn.views.tuchwith'),      
    (r'variant-lines/$', 'gutorglyn.views.variantLines'),      
    (r'www/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'www'}),
    (r'search-test/$', 'gutorglyn.views.searchTest'),
    #(r'poem/(?P<poem>[^/]+)$', 'gutorglyn.views.poem'),    
                       
    # Example:

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    #Text:
)
