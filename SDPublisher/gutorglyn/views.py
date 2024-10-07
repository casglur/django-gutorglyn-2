# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *
from pixelise.core import Collection
import math

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from django.utils.encoding import smart_str
from django.utils.translation import ugettext as _

from gutorglyn.models import manuscripts
from gutorglyn.models import manuscriptSort
from gutorglyn.models import personalNames
from gutorglyn.models import placeNames
from gutorglyn.models import poemSort

import re

from httplib import HTTPResponse

# URLS
baseURL                 =   'gutorglyn/'
errorURL                =   baseURL + 'error.html'
servicePixelateURL      =   baseURL + 'base-raw.py'

# Constants
poemOrderSequence = ('001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018a', '018', '019', '020', '020a', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '044a', '045', '046', '046a', '046b', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065a', '065','066', '067', '068a', '068', '068b','069', '070', '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082', '083', '084', '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '098', '099', '100', '101a', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126')

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def aboutProject(request):
    lang = request.COOKIES.get('gutorglynlang', '')
    lang = getLang(lang)                     
    return render_to_response('gutorglyn/about.html', {'lang': lang})    

def allPatrons(request):
    lang = request.COOKIES.get('gutorglynlang', '')
    lang = getLang(lang)     
    p = Collection(request, 'gutorglyn')
    patronNames = p.complex_query('for $x in collection("gutorglyn.bdbxml")//tei:div[@type="nodyn_noddwr"] order by $x/tei:div[@type="%s"]/tei:head return <patron id="{$x/@xml:id/data(.)}">{$x/tei:div[@type="%s"]/tei:head}</patron>' % (str(lang),str(lang)))
    
    patronNamesOutput = ""
    
    while patronNames.hasNext():
        patronNamesValues = patronNames.next()
        patronNamesOutput += p.process_element(patronNamesValues, 'gutorglyn/patrons.py', False, None)     
        
    return render_to_response('gutorglyn/patron-list.html', {'patronNamesOutput': patronNamesOutput})    
#     return render_to_response('gutorglyn/patron-list.html',)

def allPatronsJSON(request):
    lang = request.COOKIES.get('gutorglynlang', '')
    lang = getLang(lang)     
    p = Collection(request, 'gutorglyn')
    patronNames = p.complex_query('for $x in collection("gutorglyn.bdbxml")//tei:div[@type="nodyn_noddwr"] order by $x/tei:div[@type="%s"]/tei:head return $x/tei:div[@type="%s"]/tei:head' % (str(lang),str(lang)))
    patronIDs = p.complex_query('for $x in collection("gutorglyn.bdbxml")//tei:div[@type="nodyn_noddwr"] order by $x/tei:div[@type="%s"]/tei:head return <head>{$x/@xml:id/data(.)}</head>' % (str(lang)))

    patronNamesOutput = ""
    
    while patronNames.hasNext():
        patronNamesValues = patronNames.next()
        patronNamesOutput += p.process_element(patronNamesValues, 'gutorglyn/patrons-json.py', False, None) 
        
    patronIDsOutput = ""
    
    while patronIDs.hasNext():
        patronIDsValues = patronIDs.next()
        patronIDsOutput += p.process_element(patronIDsValues, 'gutorglyn/patrons-json.py', False, None)            
    
    return render_to_response('gutorglyn/patrons.json', {'patronNamesOutput': zip(patronNamesOutput.split('%'),patronIDsOutput.split('%'))}, mimetype="application/json")    

def allPatronsXML(request):
    lang = request.GET.get('lang', '')       
    p = Collection(request, 'gutorglyn')
    patronNames = p.complex_query('<patrons>{for $x in collection("gutorglyn.bdbxml")//tei:div[@type="nodyn_noddwr"] order by $x/tei:div[@type="%s"]/tei:head return <patron><id>{$x/@xml:id/data(.)}</id><name>{$x/tei:div[@type="%s"]/tei:head/descendant-or-self::text()}</name></patron>}</patrons>' % (str(lang),str(lang)))
    #names = p.query('//tei:div[@type="nodyn_noddwr"]')
    #names = p.complex_query('let $range := (1 to 3) return collection("gutorglyn.bdbxml")//tei:div[@xml:id="Guto001testun"]/tei:lg/tei:l[@n=$range]')   
    
    #editedText = p.complex_query('for $lines in collection("gutorglyn.bdbxml")//tei:div[@type="lev1"]/tei:lg where some $line in $lines satisfies (dbxml:contains($line, "Ond")) return $lines')    
    
    patronNamesOutput = ""
    
    while patronNames.hasNext():
        patronNamesValues = patronNames.next()
        patronNamesOutput += p.process_element(patronNamesValues, 'gutorglyn/patrons-xml.py', False, None)   
    
    return render_to_response('gutorglyn/patrons-xml.xml', {'patronNamesOutput': patronNamesValues}, mimetype="application/xml")

def biog(request):
    cookieLang = request.COOKIES.get('gutorglynlang')
    lang = getLang(cookieLang)
       
    return render_to_response('gutorglyn/biog.html', {'lang': lang})

def docListDropdown(request):
    mgr = XmlManager()
    container = mgr.openContainer("gutorglyn/gutorglyn.bdbxml")
    results = container.getAllDocuments(0)
    
    docList = []
    for value in results:
        doc = value.asDocument()
        docs = doc.getName()
        docList.append(docs)  
    
    return render_to_response('gutorglyn/manage/xml-upload.html', {'documents': docList})    

def drwmConcert(request):
    return render_to_response('gutorglyn/drwm-videos.html',)   

def essays(request):
    return render_to_response('gutorglyn/essays.html',)

def getName(request, personID=None, placeID=None):
    cookieLang = request.COOKIES.get('gutorglynlang')
    lang = getLang(cookieLang)
    nameType = None
    personID = request.GET.get('personID', '')
    placeID = request.GET.get('placeID', '')
    
    if personID:
        nameDetails = personalNames.objects.filter(name_id=personID).values('def_cym', 'def_eng', 'name_in_text', 'line_ref').order_by('line_ref', 'name_in_text')
        nameType = 'person'    
    
    if placeID:
        nameDetails = placeNames.objects.filter(place_id=placeID).values('def_cym', 'def_eng', 'place_in_text', 'line_ref').order_by('line_ref', 'place_in_text')
        nameType = 'place'            
    
    return render_to_response('gutorglyn/name-db.html', {'lang':lang, 'nameDetails':nameDetails, 'nameType':nameType })   

def getPersonalNames(request):
    nameList = personalNames.objects.all().order_by('name_in_text')
    return render_to_response('gutorglyn/personal-names-db.html', {'nameList':nameList})

def getPlaceNames(request):
    placeList = placeNames.objects.all().order_by('place_in_text')
    return render_to_response('gutorglyn/place-names-db.html', {'placeList': placeList})

def getPoem(request):
    if request.GET.get('searchVal', ''):
        searchStr = request.GET.get('searchVal', '')
    elif request.GET.get('search-title', ''):
        searchStr = request.GET.get('search-title', '')
        
    searchStr = searchStr.replace(u"\u2013","-")
    searchStr = repr(searchStr)
    searchStr = searchStr.replace(" ", "")
    number = searchStr.split('-')[0]
    
    number = number.strip()
    
    number = number.decode('utf-8')
    
    number = number.replace("u'","")
    
    numLength = len(number)
    
    if numLength == 1:
        number =  '00' + number
   
    elif numLength == 2:
        number =  '0' + number
    
    elif numLength >= 3:
        number = number
    
    return HttpResponseRedirect ('/gutorglyn/poem/?poem-selection=' + str(number))
      
    
def getLang(lang):
    if lang == 'en-GB':
        return 'eng'
    else:
        return 'cym'  
    
def guidelines(request):                    
    return render_to_response('gutorglyn/guidelines.html',)       
    
def index(request):
    cookieLang = request.COOKIES.get('gutorglynlang')                    
    return render_to_response('gutorglyn/index.html', {'lang': cookieLang})

def indexNew(request):                      
    return render_to_response('gutorglyn/bootstrap/base.html',)

def getManuscripts(request):
    cookieLang = request.COOKIES.get('gutorglynlang')
    lang = getLang(cookieLang)
    
    action_def = ''
    hand = ''
    manu_ID = request.GET.get('m', '')
    manu_list = ''
    poem_ID = request.GET.get('p', '')  
    poem_list = '' 
          
    manu_select = manuscriptSort.objects.values('manuscript_name').order_by('sort_order').distinct()
#     manu_select = manuscripts.objects.raw('SELECT distinct id, manuscript FROM gutorglyn_manuscripts order by manuscript')
    
    poem_select = poemSort.objects.values('poem_number').order_by('sort_order').distinct()
    
    if (poem_ID):
        action_def = _("Searching for manuscripts containing poem number") + poem_ID
        manu_list = manuscripts.objects.filter(poem_number=poem_ID)
    if (manu_ID):
        action_def = _("Searching for poems contained in manuscripts reference") + manu_ID
        poem_list = manuscripts.objects.filter(manuscript=manu_ID).order_by('poem_number')
    
    return render_to_response('gutorglyn/manuscripts-db.html', {'action_def': action_def, 'manu_list': manu_list,'manu_select': manu_select, 'poem_list': poem_list, 'poem_select': poem_select, 'lang': lang})

def getManuscriptsSources(request):
    cookieLang = request.COOKIES.get('gutorglynlang')
    lang = getLang(cookieLang)
    
    action_def = ''
    hand = ''
    manu_ID = request.GET.get('m', '')
    manu_list = ''
    poem_ID = request.GET.get('p', '')  
    poem_list = '' 
          
    manu_select = manuscriptSort.objects.values('manuscript_name').order_by('sort_order').distinct()
    
    poem_select = poemSort.objects.values('poem_number').order_by('sort_order').distinct()
    
    if (poem_ID):
        action_def = _("Searching for manuscripts containing poem number") + poem_ID
        manu_list = manuscripts.objects.filter(poem_number=poem_ID)
    if (manu_ID):
        action_def = _("Searching for poems contained in manuscripts reference") + manu_ID
        poem_list = manuscripts.objects.filter(manuscript=manu_ID).order_by('poem_number')
    
    return render_to_response('gutorglyn/manuscripts-db-sources.html', {'action_def': action_def, 'manu_list': manu_list,'manu_select': manu_select, 'poem_list': poem_list, 'poem_select': poem_select, 'lang': lang})


def musicalCompanions(request):
    return render_to_response('gutorglyn/musical-companions.html',)  

def name(request):
    urlLang = request.GET.get('lang')
    cookieLang = request.COOKIES.get('gutorglynlang')
    nameRequest = request.GET.get(r'n', '') 
    
    lang = ""
    if urlLang <= "":
        lang = cookieLang
        lang = getLang(cookieLang)
    else:
        lang = urlLang
    
    p = Collection(request, 'gutorglyn')
    names = p.query('//tei:div[@type="nodyn_noddwr" and @xml:id="%s"]/tei:div[@type="%s"]' % (nameRequest,lang))
    
    if names.hasNext():
        namesValues = names.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find name " + nameRequest})
    namesText = p.process_element(namesValues, 'gutorglyn/base.py', False, None)
    
    return render_to_response('gutorglyn/name.html', {'name': namesText})

def nameFull(request):
    urlLang = request.GET.get('lang')
    cookieLang = request.COOKIES.get('gutorglynlang')
    nameRequest = request.GET.get(r'n', '') 
    
    lang = ""
    if urlLang <= "":
        lang = cookieLang
        lang = getLang(cookieLang)
    else:
        lang = urlLang
    
    p = Collection(request, 'gutorglyn')
    names = p.query('//tei:div[@type="nodyn_noddwr" and @xml:id="%s"]/tei:div[@type="%s"]' % (nameRequest,lang))
    
    if names.hasNext():
        namesValues = names.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find name " + nameRequest})
    namesText = p.process_element(namesValues, 'gutorglyn/base.py', False, None)
    
    return render_to_response('gutorglyn/patron-detail.html', {'name': namesText})

def patrons(request):
    
    lang = request.GET.get('lang', '')
    lang = getLang(lang) 
        
    nameRequest = request.GET.get(r'n', '') 
    
    p = Collection(request, 'gutorglyn')
    nameDetail = p.query('//tei:div[@type="nodyn_noddwr" and @xml:id="%s"]/tei:div[@type="%s"]' % (nameRequest, lang))
    
    if nameDetail.hasNext():
        nameDetailValues = nameDetail.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find name " + nameRequest})
    nameDetailText = p.process_element(nameDetailValues, 'gutorglyn/base.py', False, None)
    
    return render_to_response('gutorglyn/patron-panel.html', {'nameDetail': nameDetailText})
    
def people(request):
    #poemNum = '018a'
    poem = request.GET.get(r'poem', '')
    
    p = Collection(request, 'gutorglyn')
    peopleDetail = p.complex_query('for $x in collection("gutorglyn.bdbxml")//tei:div[@xml:id="Guto%stop"]/tei:div[@type="pobl"]/tei:note, $y in collection("gutorglyn.bdbxml")//tei:div where data($x) = data($y/@xml:id) return $y/tei:div[@type="eng"]/child::node()' % (str(poem)))
    
    #if peopleDetail.hasNext():
    #    peopleDetailValues = peopleDetail.next()
    #else:
    #    return render_to_response('gutorglyn/error.html', {'message': "Can't find name IDs"})
    #peopleDetailText = p.process_element(peopleDetailValues, 'gutorglyn/base.py', False, None)
    
    peopleDetailText = ""
     
    while peopleDetail.hasNext():
        peopleDetailValues = peopleDetail.next()
        peopleDetailText += p.process_element(peopleDetailValues, 'gutorglyn/base.py', False, None)
    
    return render_to_response('gutorglyn/patron-panel.html', {'peopleDetail': peopleDetailText})  

# Views for functions # 

def poem(request, poem=None):
    lang = request.COOKIES.get('gutorglynlang', '')
    lang = getLang(lang)
    
    poemCookie = request.COOKIES.get('gutorglynpoem', '')

    poem = str(request.GET.get(r'poem-selection', ''))
    
    if poem == '' and poemCookie == '':
        poem = '001'
    elif poem == '' and poemCookie is not None:                
        poem = poemCookie
    else:
        poem = poem
    
    if poem == '':
        poem = request.GET.get(r'first-line', '')
    
            
    if poem.find('.'):
        poem_array = poem.split('.')
        poem = poem_array[0]    
        
    poemLength = len(poem)        
    
    if poemLength == 1:
        poem = '00' + poem
    elif poemLength == 2:
        poem = '0' + poem

    if poemLength == 3:
        if poem.isdigit():
            poem = poem
        else:
            poem = '0' + poem
              
    #if request.GET.get(r'poem', '') == '':
    #       poem = "%s" % (poem)
    #else:
    #      poem = request.GET.get(r'poem', '')
    # 
    p = Collection(request, 'gutorglyn')     
    
    poemTitle = p.query('//tei:div[@xml:id="Guto%stop"]/tei:head' % (str(poem))) 
    
    if lang == 'cym':
        poemTitle = p.query('//tei:div[@xml:id="Guto%stop"]/tei:head' % (str(poem)))   
    elif lang == 'eng':
        poemTitle = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[3]/tei:lg[1]/tei:l[1]' % (str(poem)))  
        
    editedText = p.query('//tei:div[@xml:id="Guto%stestun"]' % (str(poem)))
    paraphrase = p.query('//tei:div[@xml:id="Guto%saralleiriad"]' % (str(poem)))
    translation = p.query('//tei:div[@xml:id="Guto%stranslation"]' % (str(poem)))
    textNotes = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Testunol"]' % (str(poem)))
    exNotes = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Esboniadol"]' % (str(poem)))  
    exEngNotes = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Explanatory"]' % (str(poem)))
    editor =  p.query('//tei:div[@xml:id="Guto%stop"]/tei:note[@type="golygydd"]' % (str(poem)))
    peopleDetail = p.complex_query('for $x in collection("gutorglyn.bdbxml")//tei:div[@xml:id="Guto%stop"]/tei:div[@type="pobl"]/tei:note, $y in collection("gutorglyn.bdbxml")//tei:div where data($x) = data($y/@xml:id) return $y/tei:div[@type="%s"]/child::node()' % (str(poem),lang))
    peopleLinks = p.complex_query('for $x in collection("gutorglyn.bdbxml")//tei:div[@xml:id="Guto%stop"]/tei:div[@type="pobl"]/tei:note, $y in collection("gutorglyn.bdbxml")//tei:div where data($x) = data($y/@xml:id) return <a href="#{$x}">{$y/tei:div[@type="%s"]/tei:head/text()}</a>' % (str(poem),lang))

    poemNumbers = p.query('/tei:div/@xml:id')    
    
    if poemTitle.hasNext():
        poemTitleValues = poemTitle.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find poemTitle"})
    text_content = p.process_element(poemTitleValues, 'gutorglyn/base.py', False, None)  
#     text_content = poemTitleValues         
    
    if editedText.hasNext():
        editedTextValues = editedText.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find editedText"})
    text_content1 = p.process_element(editedTextValues, 'gutorglyn/base.py', False, None)  
    
    if paraphrase.hasNext():
        paraphraseValues = paraphrase.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find paraphrase"})
    text_content2= p.process_element(paraphraseValues, 'gutorglyn/base.py', False, None)
     
    if translation.hasNext():
        translationValues = translation.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find translation"})
    text_content3= p.process_element(translationValues, 'gutorglyn/base.py', False, None)
    
    if textNotes.hasNext():
        textNotesValues = textNotes.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find textNotes"})
    text_content4 = p.process_element(textNotesValues, 'gutorglyn/base.py', False, None)  
    
    if exNotes.hasNext():
        exNotesValues = exNotes.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find exNotes"})
    text_content5 = p.process_element(exNotesValues, 'gutorglyn/base.py', False, None)       
    
    if exEngNotes.hasNext():
        exEngNotesValues = exEngNotes.next()
        text_content6 = p.process_element(exEngNotesValues, 'gutorglyn/ex_eng_notes.py', False, None)
    else:
        exEngNotesValues = "XML Source Error - There are no English Explanatory notes in the source XML"
        #return render_to_response('gutorglyn/error.html', {'message': "Can't find exEngNotes"})     
        text_content6 = exEngNotesValues
    
    if editor.hasNext():
        editorValues = editor.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find editor"})
    text_content7 = p.process_element(editorValues, 'gutorglyn/base.py', False, None)
    
    peopleDetailText = ""
     
    while peopleDetail.hasNext():
        peopleDetailValues = peopleDetail.next()
        peopleDetailText += p.process_element(peopleDetailValues, 'gutorglyn/patron.py', False, None)

    peopleLinksText = ""

    while peopleLinks.hasNext():
        peopleLinksValues = peopleLinks.next()
        peopleLinksText += p.process_element(peopleLinksValues, 'gutorglyn/patron.py', False, None)   
    
    poemNumbersText = ""
    
    while poemNumbers.hasNext():
        thisPoemNumberLine = poemNumbers.next()
        poemNumbersText += p.process_element(thisPoemNumberLine, 'gutorglyn/base.py', False, None)
    
    return render_to_response('gutorglyn/poem.html', {                                                      
                                                        'editor': text_content7,                                                      
                                                        'editedText': text_content1,
                                                        'paraphrase': text_content2, 
                                                        'translation': text_content3, 
                                                        'textNotes': text_content4,  
                                                        'exNotes': text_content5,  
                                                        'exEngNotes': text_content6,
                                                        'lang': lang,
                                                        'patron': peopleDetailText,
                                                        'patronIds':peopleLinksText,
                                                        'poemNumber': poem,
                                                        'poemNumbers': poemNumbersText,
                                                        'poem_page_title': re.sub('<[^<]+?>', '', text_content),
                                                        'poemTitle': text_content,                                                                                 
                                                        }, mimetype="text/html")

def printThis(request):                    
    return render_to_response('gutorglyn/print-this.html',)  


def rawLines(request, poem=None, lg=None):
    p = Collection(request, 'gutorglyn')       
    
    if lg == 0:
        editedText = p.query('//tei:div[@xml:id="Guto%stestun"]' % (poem))
    else:
        editedText = p.query('//tei:div[@xml:id="Guto%stestun"]/tei:lg[@n="%s"]' % (poem,lg))
        
    if lg == 0:
        paraphrase = p.query('//tei:div[@xml:id="Guto%saralleiriad"]' % (poem))        
    else:
        paraphrase = p.query('//tei:div[@xml:id="Guto%saralleiriad"]/tei:lg[@n="%s"]' % (poem,lg))        
        
    if lg == 0:
        translation = p.query('//tei:div[@xml:id="Guto%stranslation"]' % (poem))        
    else:
        translation = p.query('//tei:div[@xml:id="Guto%stranslation"]/tei:lg[@n="%s"]' % (poem,lg))             
    
    if editedText.hasNext():
        editedTextValues = editedText.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find editedText"})
    editedTextLg = p.process_element(editedTextValues, 'gutorglyn/base-raw.py', False, None)  
    
    if paraphrase.hasNext():
        paraphraseValues = paraphrase.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find paraphrase"})
    paraphraseLg = p.process_element(paraphraseValues, 'gutorglyn/base-raw.py', False, None)
     
    if translation.hasNext():
        translationValues = translation.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find translation"})
    translationLg = p.process_element(translationValues, 'gutorglyn/base-raw.py', False, None)    
        
    return render_to_response('gutorglyn/lines-raw.html', {
                                                            'editedTextLg': editedTextLg,
                                                            'paraphraseLg': paraphraseLg, 
                                                            'translationLg': translationLg,                                                                                         
                                                            })
    
    
def rawLinesRange(request, poem=None, startline=None, endline=None):
    p = Collection(request, 'gutorglyn')       
    
    editedText = p.complex_query('let $range := (1 to 3) return collection("gutorglyn.bdbxml")//tei:div[@xml:id="Guto001testun"]/tei:lg/tei:l[@n=$range]')
    #editedText = p.query('//tei:div[@xml:id="Guto%stestun"]/tei:lg[@n="%s"]' % (poem,startline))                  
    
    editedTextLg = ""
    
    while editedText.hasNext():
        editedTextValues = editedText.next()
        editedTextLg += p.process_element(editedTextValues, 'gutorglyn/base-raw.py', False, None)       
        
    return render_to_response('gutorglyn/lines-raw.html', {
                                                            'editedTextLg': editedTextLg,                                                                                        
                                                            })
    

def rawLine(request, poem=None, line=None):
    p = Collection(request, 'gutorglyn')     
    
    if line == 0:
        editedText = p.query('//tei:div[@xml:id="Guto%stestun"]' % (poem))
    else:
        editedText = p.query('//tei:div[@xml:id="Guto%stestun"]/tei:lg/tei:l[@n="%s"]' % (poem,line))
        
    if line == 0:
        paraphrase = p.query('//tei:div[@xml:id="Guto%saralleiriad"]' % (poem))        
    else:
        paraphrase = p.query('//tei:div[@xml:id="Guto%saralleiriad"]/tei:lg/tei:l[@n="%s"]' % (poem,line))        
        
    if line == 0:
        translation = p.query('//tei:div[@xml:id="Guto%stranslation"]' % (poem))        
    else:
        translation = p.query('//tei:div[@xml:id="Guto%stranslation"]/tei:lg/tei:l[@n="%s"]' % (poem,line))             
    
    if editedText.hasNext():
        editedTextValues = editedText.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find editedText"})
    editedTextLine = p.process_element(editedTextValues, 'gutorglyn/base-raw.py', False, None)  
    
    if paraphrase.hasNext():
        paraphraseValues = paraphrase.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find paraphrase"})
    paraphraseLine = p.process_element(paraphraseValues, 'gutorglyn/base-raw.py', False, None)
     
    if translation.hasNext():
        translationValues = translation.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find translation"})
    translationLine = p.process_element(translationValues, 'gutorglyn/base-raw.py', False, None)    
        
    return render_to_response('gutorglyn/line-raw.html', {
                                                            'editedTextLine': editedTextLine,
                                                            'paraphraseLine': paraphraseLine, 
                                                            'translationLine': translationLine,                                                                                         
                                                            })

def rawParts(request, poem=None):
    poemPart = request.GET.get('poem-part', '')
    p = Collection(request, 'gutorglyn')     
    
    poemTitle = p.query('//tei:div[@xml:id="Guto%stop"]/tei:head' % (str(poem)))   
    editedText = p.query('//tei:div[@xml:id="Guto%stestun"]' % (str(poem)))
    paraphrase = p.query('//tei:div[@xml:id="Guto%saralleiriad"]' % (str(poem)))
    translation = p.query('//tei:div[@xml:id="Guto%stranslation"]' % (str(poem)))
    textNotes = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Testunol"]' % (str(poem)))
    exNotes = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Esboniadol"]' % (str(poem)))  
    exEngNotes = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Explanatory"]' % (str(poem)))
    editor =  p.query('//tei:div[@xml:id="Guto%stop"]/tei:note[@type="golygydd"]' % (str(poem)))
    
    if poemTitle.hasNext():
        poemTitleValues = poemTitle.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find poemTitle"})
    poemTitlePart = p.process_element(poemTitleValues, 'gutorglyn/base-raw.py', False, None)      
    
    if editedText.hasNext():
        editedTextValues = editedText.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find editedText"})
    editedTextPart = p.process_element(editedTextValues, 'gutorglyn/base-raw.py', False, None)  
    
    if paraphrase.hasNext():
        paraphraseValues = paraphrase.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find paraphrase"})
    paraphrasePart = p.process_element(paraphraseValues, 'gutorglyn/base-raw.py', False, None)
     
    if translation.hasNext():
        translationValues = translation.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find translation"})
    translationPart = p.process_element(translationValues, 'gutorglyn/base-raw.py', False, None)
    
    if textNotes.hasNext():
        textNotesValues = textNotes.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find textNotes"})
    textNotesPart = p.process_element(textNotesValues, 'gutorglyn/base-raw.py', False, None)  
    
    if exNotes.hasNext():
        exNotesValues = exNotes.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find exNotes"})
    exNotesPart = p.process_element(exNotesValues, 'gutorglyn/base-raw.py', False, None)       
    
    if exEngNotes.hasNext():
        exEngNotesValues = exEngNotes.next()
        exEngNotesPart = p.process_element(exEngNotesValues, 'gutorglyn/base-raw.py', False, None)
    else:
        exEngNotesValues = "XML Source Error - There are no English Explanatory notes in the source XML"
        #return render_to_response('gutorglyn/error.html', {'message': "Can't find exEngNotes"})     
        exEngNotesPart = exEngNotesValues
    
    if editor.hasNext():
        editorValues = editor.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find editor"})
    editorPart = p.process_element(editorValues, 'gutorglyn/base-raw.py', False, None)       
    
    return render_to_response('gutorglyn/raw-part.html', {'poemPart': eval(poemPart + 'Part')})

def rawPoem(request, poem=None):
    print "%s" % (poem)
    
    #if request.GET.get(r'poem', '') == '':
    #       poem = "%s" % (poem)
    #else:
    #      poem = request.GET.get(r'poem', '')
    # 
    p = Collection(request, 'gutorglyn')     
    
    poemTitle = p.query('//tei:div[@xml:id="Guto%stop"]/tei:head' % (str(poem)))   
    editedText = p.query('//tei:div[@xml:id="Guto%stestun"]' % (str(poem)))
    paraphrase = p.query('//tei:div[@xml:id="Guto%saralleiriad"]' % (str(poem)))
    translation = p.query('//tei:div[@xml:id="Guto%stranslation"]' % (str(poem)))
    textNotes = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Testunol"]' % (str(poem)))
    exNotes = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Esboniadol"]' % (str(poem)))  
    exEngNotes = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Explanatory"]' % (str(poem)))
    editor =  p.query('//tei:div[@xml:id="Guto%stop"]/tei:note[@type="golygydd"]' % (str(poem)))
    
    if poemTitle.hasNext():
        poemTitleValues = poemTitle.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find poemTitle"})
    text_content = p.process_element(poemTitleValues, 'gutorglyn/base-raw.py', False, None)      
    
    if editedText.hasNext():
        editedTextValues = editedText.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find editedText"})
    text_content1 = p.process_element(editedTextValues, 'gutorglyn/base-raw.py', False, None)  
    
    if paraphrase.hasNext():
        paraphraseValues = paraphrase.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find paraphrase"})
    text_content2= p.process_element(paraphraseValues, 'gutorglyn/base-raw.py', False, None)
     
    if translation.hasNext():
        translationValues = translation.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find translation"})
    text_content3= p.process_element(translationValues, 'gutorglyn/base-raw.py', False, None)
    
    if textNotes.hasNext():
        textNotesValues = textNotes.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find textNotes"})
    text_content4 = p.process_element(textNotesValues, 'gutorglyn/base-raw.py', False, None)  
    
    if exNotes.hasNext():
        exNotesValues = exNotes.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find exNotes"})
    text_content5 = p.process_element(exNotesValues, 'gutorglyn/base-raw.py', False, None)       
    
    if exEngNotes.hasNext():
        exEngNotesValues = exEngNotes.next()
        text_content6 = p.process_element(exEngNotesValues, 'gutorglyn/base-raw.py', False, None)
    else:
        exEngNotesValues = "XML Source Error - There are no English Explanatory notes in the source XML"
        #return render_to_response('gutorglyn/error.html', {'message': "Can't find exEngNotes"})     
        text_content6 = exEngNotesValues
    
    if editor.hasNext():
        editorValues = editor.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find editor"})
    text_content7 = p.process_element(editorValues, 'gutorglyn/base-raw.py', False, None)       
    
    return render_to_response('gutorglyn/poem-raw.html', {'poemTitle': text_content,
                                                            'editedText': text_content1,
                                                            'paraphrase': text_content2, 
                                                            'translation': text_content3, 
                                                            'textNotes': text_content4,  
                                                            'exNotes': text_content5,  
                                                            'exEngNotes': text_content6,
                                                            'editor': text_content7                                                                                             
                                                            })

def searchMaster(request):
        
    searchStr = request.GET.get('searchVal', '')
    searchStr = searchStr.replace("'", u"\u2019")
    myContainer = Collection(request, 'gutorglyn')    
    myQuery = 'for $lines in collection(\'gutorglyn.bdbxml\')//tei:div[@type=\'lev1\']/tei:lg/tei:l where some $line in $lines satisfies (dbxml:contains($line, "%s")) return $lines' % (smart_str(searchStr))
    results = myContainer.complex_query(myQuery)
        
    hitList = {}
    count = 0
    for value in results:
        document = value.asDocument()
        name = document.getName()
        content = value.asString()
        count +=1
        hitList[name+'('+(str(count))+')'] = content         
    
    #send_result = myContainer.process_element(hitList, 'gutorglyn/base.py', False, None)            
    return render_to_response('gutorglyn/searchResults.html', {'searchHits': hitList,
                                                               'searchNum': count,
                                                               'searchTrm': searchStr,
                                                               })
    
def search(request):
    return render_to_response('gutorglyn/search.html',)
        
def searchResults(request):
    debug_flag = request.GET.get('debug', '')
    cookieLang = request.COOKIES.get('gutorglynlang') 
    ignoreDiacriticsFlag = request.GET.get('ignore-diacritics', '')
    
    lang = getLang(cookieLang)
    
    searchOption = request.GET.get('search-option', '')
    
    matchCaseFlag = request.GET.get('match-case', '')
    regExFlag = request.GET.get('reg-ex', '')
    
    if request.GET.get('searchVal', ''):
        searchStr = request.GET.get('searchVal', '')
    elif request.GET.get('advanced-q', ''):
        searchStr = request.GET.get('advanced-q', '')
    else:    
        searchStr = None
                
    searchStr = searchStr.replace("'", u"\u2019") # replace right single quotation mark 
    
    if request.GET.get('per-page', ''):
        perPage = int(request.GET.get('per-page', ''))
    else:
        perPage = int(10)
                      
    if request.GET.get('page-start', ''):
        pageStart = int(request.GET.get('page-start', '')) + 1
        pageEnd = pageStart + perPage - 1
    else: 
        pageStart = int(0)        
        pageEnd = pageStart + perPage 
        
    wholeWordFlag = request.GET.get('whole-word', '')    
    
    containsType = None
    functionText = None
    searchType = None    
    stringMatch = None
    xqueryFunction = None
    
#     if matchCaseFlag == "":
#         containsType = "dbxml:contains"
#         searchType = _("Search Type Definition case-insensitive")
#         regExCaseFlag = 'i' 
#     else:
#         containsType = "contains"
#         searchType = _("Search Type Definition case-sensitive")
#         regExCaseFlag = ''        
#  
#     if ignoreDiacriticsFlag == "on":
#         stringMatch = "smart_str"
#         searchType = searchType + ' - ' + _("Search Type Definition ignoring diacritics")
#     else:
#         stringMatch = ""

    stringMatch = ""
    
    if searchOption == "match-case":
        containsType = "contains"
        searchType = _("Search Type Definition case-sensitive")
    
    if searchOption == "ignore-diacritics":
        containsType = "dbxml:contains"
        stringMatch = "smart_str"
        searchType = _("Search Type Definition case-insensitive") + ' - ' + _("Search Type Definition ignoring diacritics")

    
    p = Collection(request, 'gutorglyn')
    
#     XML Paths for Xquery function
    explanatory_notes_nodes = 'collection("gutorglyn.bdbxml")//tei:div[@type="Esboniadol"]/tei:note'
    explanatory_notes_xml_id = '/../@xml:id'
    explanatory_notes_title = '/../../tei:head'
    paraphrases_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[2]/tei:lg'
    paraphrases_xml_id = '/../@xml:id'
    paraphrases_title = '/../../tei:head'
    
    if regExFlag == "on":
        poem_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg/tei:l'
    else:
        poem_nodes = 'collection("gutorglyn.bdbxml")//tei:div[@type="lev1"]/tei:lg' 
    
    poem_xml_id = '/../@xml:id'
    poem_title = '/../../tei:head'    
    sources_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[7]/tei:div[1]/tei:div[1]/tei:lg'
    sources_xml_id = '/../../../../@xml:id'
    sources_title = '/../tei:head'
    translations_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[3]/tei:lg'
    translations_xml_id = '/../@xml:id'
    translations_title = '/../../tei:head'
    
    expNotesCount = 0
    namesCount = 0
    paraphraseCount = 0
    poemCount = 0
    sourcesCount = 0
    textNotesCount = 0
    transCount = 0  
    
    expNotesSearchLineGroupResultsText = ""
    namesSearchLineGroupResultsText = ""      
    paraphraseSearchLineGroupResultsText = ""
    poemSearchLineGroupResultsText = ""  
    poemSearchLineResultsText = ""      
    sourcesSearchLineGroupResultsText = ""      
    textNotesSearchLineGroupResultsText = ""      
    transSearchLineGroupResultsText = ""
    
    if searchOption == "reg-ex":
        searchType = _("Search Type Definition regular expression") + ' - ' + _("Search Type Definition case-sensitive")

        poemSearchLineResults = p.complex_query('\
         declare variable $query := "%s"; \
         declare variable $poem_nodes as node()* := collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg/tei:l; \
         let $start := 0 \
         let $end := %s \
         for $x at $i in $poem_nodes[matches(., $query)] \
         return $x[$i = ($start to $end)] \
            ' % (smart_str(searchStr), pageEnd))      

        poemSearchLineResultsCount = p.complex_query('\
            declare variable $query := "%s"; \
            declare variable $poem_nodes as node()* := %s; \
            let $total := count($poem_nodes[matches(., $query)]) \
            return $total \
            ' % (smart_str(searchStr), poem_nodes))                   
           
        while poemSearchLineResults.hasNext():
            poemSearchLineValues = poemSearchLineResults.next()
            poemSearchLineResultsText += p.process_element(poemSearchLineValues, 'gutorglyn/search_results_reg_ex.py', False, None)
            poemCount += 1
            
        while poemSearchLineResultsCount.hasNext():
            poemSearchLineResultsCountValue = poemSearchLineResultsCount.next()
            poemSearchLineResultsCountNumber = int(poemSearchLineResultsCountValue.asString())
            totalPageNum = math.ceil(float(poemSearchLineResultsCountNumber)/int(perPage))
            
        if poemSearchLineResultsCountNumber < pageEnd:
            pageEnd = poemSearchLineResultsCountNumber                     

        return render_to_response('gutorglyn/searchResultsNew.html', {     
                                                       'debug': debug_flag,                                                                          
                                                       'pageStart': pageStart,
                                                       'pageEnd': pageEnd,
                                                       'perPage': perPage,                                                                                                                          
                                                       'poemSearchGroupHits': poemSearchLineGroupResultsText,
                                                       'poemSearchLineHits': poemSearchLineResultsText,
                                                       'poemSearchNum': poemSearchLineResultsCountNumber,
                                                       'searchOption': searchOption,
                                                       'searchTrm': searchStr,
                                                       'searchType': searchType,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                       })              

#     Search Using 'Contains'
############################## 
    else:
        poemSearchLineResultsCount = p.complex_query('\
            declare variable $query := "%s"; \
            declare variable $poem_nodes as node()* := %s; \
            let $total := count($poem_nodes[%s(., $query)]) \
            return $total \
            ' % (smart_str(searchStr), poem_nodes, containsType))                   
            
        while poemSearchLineResultsCount.hasNext():
            poemSearchLineResultsCountValue = poemSearchLineResultsCount.next()
            poemSearchLineResultsCountNumber = int(poemSearchLineResultsCountValue.asString())
            totalPageNum = math.ceil(float(poemSearchLineResultsCountNumber)/int(perPage))

            
        pageValuesList = []
        for i in range(0, int(totalPageNum) * int(perPage) + 1, int(perPage)):
            pageValuesList.append(i)  
            
        try:
            currentPoemPageNumber = pageValuesList.index(pageEnd)
        except:
            currentPoemPageNumber = '1'                          
        
        expNotesSearchLineGroupResults = p.complex_query(searchNotesXquery(searchStr, explanatory_notes_nodes, explanatory_notes_xml_id, explanatory_notes_title, containsType, pageEnd, pageStart))
        namesSearchLineGroupResults = p.complex_query('for $lines in collection("gutorglyn.bdbxml")//tei:div[@type="nodyn_noddwr"]/tei:div[@type="%s"]/tei:p where some $line in $lines satisfies (%s($line, "%s")) return $lines' % (lang, containsType, smart_str(searchStr)))

        paraphraseSearchLineGroupResults = p.complex_query(searchXquery(searchStr, paraphrases_nodes, paraphrases_xml_id, paraphrases_title, containsType, pageEnd, pageStart))              
        poemSearchLineResults = p.complex_query(searchXquery(searchStr, poem_nodes, poem_xml_id, poem_title, containsType, pageEnd, pageStart))
          
        sourcesSearchLineGroupResults = p.complex_query(searchXquery(searchStr, sources_nodes, sources_xml_id, sources_title, containsType, pageEnd, pageStart))       
        textNotesSearchLineGroupResults = p.complex_query('for $lines in collection("gutorglyn.bdbxml")//tei:div[@type="Testunol"]/tei:note/tei:p where some $line in $lines satisfies (%s($line, "%s")) return $lines' % (containsType, smart_str(searchStr)))
        transSearchLineGroupResults = p.complex_query(searchXquery(searchStr, translations_nodes, translations_xml_id, translations_title, containsType, pageEnd, pageStart))            

        while expNotesSearchLineGroupResults.hasNext():
            expNotesSearchLineGroupValues =  expNotesSearchLineGroupResults.next()
            expNotesSearchLineGroupResultsText += p.process_element(expNotesSearchLineGroupValues, 'gutorglyn/search_results_explanatory_notes.py', False, None) 
            expNotesCount += 1                                                                                                                                                                               
        
        while namesSearchLineGroupResults.hasNext():
            namesSearchLineGroupValues = namesSearchLineGroupResults.next()
            namesSearchLineGroupResultsText += p.process_element(namesSearchLineGroupValues, 'gutorglyn/search_results_names.py', False, None) 
            namesCount += 1  
        
        while paraphraseSearchLineGroupResults.hasNext():
            paraphraseSearchLineGroupValues = paraphraseSearchLineGroupResults.next()
            paraphraseSearchLineGroupResultsText += p.process_element(paraphraseSearchLineGroupValues, 'gutorglyn/search_results_paraphrases.py', False, None) 
            paraphraseCount += 1                                                                                                                                                                                            
                  
        while poemSearchLineResults.hasNext():
            poemSearchLineValues = poemSearchLineResults.next()
            poemSearchLineResultsText += p.process_element(poemSearchLineValues, 'gutorglyn/search_results_poem.py', False, None)
            poemCount += 1            
        
        while sourcesSearchLineGroupResults.hasNext():
            sourcesSearchLineGroupValues = sourcesSearchLineGroupResults.next()
            sourcesSearchLineGroupResultsText += p.process_element(sourcesSearchLineGroupValues, 'gutorglyn/search_results_sources.py', False, None) 
            sourcesCount += 1                                                                                                                                                                                                     
        
        while textNotesSearchLineGroupResults.hasNext():
            textNotesSearchLineGroupValues =  textNotesSearchLineGroupResults.next()
            textNotesSearchLineGroupResultsText += p.process_element(textNotesSearchLineGroupValues, 'gutorglyn/search_results.py', False, None) 
            textNotesCount += 1    
    
        while transSearchLineGroupResults.hasNext():
            transSearchLineGroupValues = transSearchLineGroupResults.next()
            transSearchLineGroupResultsText += p.process_element(transSearchLineGroupValues, 'gutorglyn/search_results_translations.py', False, None) 
            transCount += 1
            
        if poemSearchLineResultsCountNumber < pageEnd:
            pageEnd = poemSearchLineResultsCountNumber        
        
        return render_to_response('gutorglyn/searchResultsNew.html', {'containsType': containsType,
                                                                   'debug': debug_flag,
                                                                   'expNotesSearchGroupHits': expNotesSearchLineGroupResultsText,   
                                                                   'expNotesSearchNum': expNotesCount,  
                                                                   'namesSearchGroupHits': namesSearchLineGroupResultsText,      
                                                                   'namesSearchNum': namesCount,
                                                                   'pageStart': pageStart,
                                                                   'pageEnd': pageEnd,                                                                                                                      
                                                                   'paraphraseSearchGroupHits': paraphraseSearchLineGroupResultsText,
                                                                   'paraphraseSearchNum': paraphraseCount,                                                               
#                                                                    'poemSearchGroupHits': poemSearchLineGroupResultsText,
                                                                   'perPage': perPage,
                                                                   'poemPageNumber': currentPoemPageNumber,
                                                                   'poemPageNumberValues': pageValuesList,
                                                                   'poemSearchLineHits': poemSearchLineResultsText,
                                                                   'poemSearchNum': poemSearchLineResultsCountNumber,      
                                                                   'searchTrm': searchStr,                                                                                                                                                                                                                                                                                                                                                              
                                                                   'textNotesSearchGroupHits': textNotesSearchLineGroupResultsText,                                                                                                   
                                                                   'textNotesSearchNum': textNotesCount,
                                                                   'transSearchGroupHits': transSearchLineGroupResultsText,   
                                                                   'transSearchNum': transCount,
                                                                   'searchOption': searchOption,                                                                   
                                                                   'searchType': searchType,
                                                                   'sourcesSearchGroupHits': sourcesSearchLineGroupResultsText,   
                                                                   'sourcesSearchNum': sourcesCount,                                                                                                                                                                              
                                                                   })                    

def searchResultsGlobal(request):
    searchMode = request.GET.get('mode', '')
    debug_flag = request.GET.get('debug', '')
    cookieLang = request.COOKIES.get('gutorglynlang') 
    ignoreDiacriticsFlag = request.GET.get('ignore-diacritics', '')    
    
    lang = getLang(cookieLang)    
    
    searchOption = request.GET.get('search-option', '')
    
    matchCaseFlag = request.GET.get('match-case', '')
    regExFlag = request.GET.get('reg-ex', '')
    
    if request.GET.get('searchVal', ''):
        searchStr = request.GET.get('searchVal', '')
    elif request.GET.get('advanced-q', ''):
        searchStr = request.GET.get('advanced-q', '')
    else:    
        searchStr = None
                
    searchStr = searchStr.replace("'", u"\u2019") # replace right single quotation mark
    searchStr = searchStr.replace("'", u"’") # replace right single quotation mark
    searchStr = searchStr.encode('ascii', 'xmlcharrefreplace')
    
    if request.GET.get('per-page', ''):
        perPage = int(request.GET.get('per-page', ''))
    else:
        perPage = int(10)
                      
    if request.GET.get('page-start', ''):
        pageStart = int(request.GET.get('page-start', '')) + 1
        pageEnd = pageStart + perPage - 1
    else: 
        pageStart = int(0)        
        pageEnd = pageStart + perPage 
        
    wholeWordFlag = request.GET.get('whole-word', '')    
    
    containsType = functionText = searchType = stringMatch = xqueryFunction = None       
    
#     if matchCaseFlag == "":
#         containsType = "dbxml:contains"
#         searchType = _("Search Type Definition case-insensitive")
#         regExCaseFlag = 'i' 
#     else:                                                  
#         containsType = "contains"
#         searchType = _("Search Type Definition case-sensitive")
#         regExCaseFlag = ''        
#  
#     if ignoreDiacriticsFlag == "on":
#         stringMatch = "smart_str"
#         searchType = searchType + ' - ' + _("Search Type Definition ignoring diacritics")
#     else:
#         stringMatch = ""        

    stringMatch = ""
    
    if searchOption == "match-case":
        containsType = "contains"
        searchType = _("Search Type Definition case-sensitive")
    
    if searchOption == "ignore-diacritics":
        containsType = "dbxml:contains"
        stringMatch = "smart_str"
        searchType = _("Search Type Definition case-insensitive") + ' - ' + _("Search Type Definition ignoring diacritics")
        
    resultsTemplate = baseURL + 'searchResultsGlobal.html'
    
#     Valuess for Xquery function
    explanatory_notes_nodes = 'collection("gutorglyn.bdbxml")//tei:div[@type="Esboniadol"]/tei:note'
    explanatory_notes_pixelate = baseURL + 'search_results_explanatory_notes.py'
    explanatory_notes_title = '/../../tei:head'
    explanatory_notes_xml_id = '/../@xml:id'    

    names_nodes = 'collection("gutorglyn.bdbxml")//tei:div[@type="nodyn_noddwr"]/tei:div[@type="%s"]/tei:p' % (lang)
    names_pixelate = baseURL + 'search_results_names.py'
    names_title = '/../../tei:head'
    names_xml_id = '/../@xml:id'    
    
    paraphrases_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[2]/tei:lg'
    paraphrases_pixelate = baseURL + 'search_results_paraphrases.py'
    paraphrases_title = '/../../tei:head'
    paraphrases_xml_id = '/../@xml:id'
        
    if regExFlag == "on":
        poem_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg/tei:l'
    else:
        poem_nodes = 'collection("gutorglyn.bdbxml")//tei:div[@type="lev1"]/tei:lg' 
    
    poem_pixelate = baseURL + 'search_results_poem.py'
    poem_title = '/../../tei:head'
    poem_xml_id = '/../@xml:id'
    
    sources_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[7]/tei:div[1]/tei:div[1]/tei:lg'
    sources_pixelate = baseURL + 'search_results_sources.py'
    sources_title = '/../tei:head'
    sources_xml_id = '/../../../../@xml:id'    
    
    text_notes_nodes = 'collection("gutorglyn.bdbxml")//tei:div[@type="Testunol"]/tei:note/tei:p'
    text_notes_pixelate = baseURL + 'search_results.py'
    text_notes_title = '/../../tei:head'    
    text_notes_xml_id = '/../@xml:id'    
    
    translations_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[3]/tei:lg'
    translations_pixelate = baseURL + 'search_results_translations.py'
    translations_title = '/../../tei:head'    
    translations_xml_id = '/../@xml:id'    
    
# dictionary for different modes - XML nodes, xml_id, xml_title, pixelate file, template file    
    searchModes = {}
    searchModes = {'explanatory_notes': {'xml_nodes': explanatory_notes_nodes, 'xml_id': explanatory_notes_xml_id, 'xml_title': explanatory_notes_title, 'pixelate': explanatory_notes_pixelate, 'template': resultsTemplate}}
    searchModes.update({'names': {'xml_nodes': names_nodes, 'xml_id': names_xml_id, 'xml_title': names_title, 'pixelate': names_pixelate, 'template': resultsTemplate}})    
    searchModes.update({'paraphrases': {'xml_nodes': paraphrases_nodes, 'xml_id': paraphrases_xml_id, 'xml_title': paraphrases_title, 'pixelate': paraphrases_pixelate, 'template': resultsTemplate}})
    searchModes.update({'poems': {'xml_nodes': poem_nodes, 'xml_id': poem_xml_id, 'xml_title': poem_title, 'pixelate': poem_pixelate, 'template': resultsTemplate}})
    searchModes.update({'sources': {'xml_nodes': sources_nodes, 'xml_id': sources_xml_id, 'xml_title': sources_title, 'pixelate': sources_pixelate, 'template': resultsTemplate}})
    searchModes.update({'text_notes': {'xml_nodes': text_notes_nodes, 'xml_id': text_notes_xml_id, 'xml_title': text_notes_title, 'pixelate': text_notes_pixelate, 'template': resultsTemplate}})   
    searchModes.update({'translations': {'xml_nodes': translations_nodes, 'xml_id': translations_xml_id, 'xml_title': translations_title, 'pixelate': translations_pixelate, 'template': resultsTemplate}})
    
    count = 0  
    
    searchLineResultsText = ""
    
    p = Collection(request, 'gutorglyn')                                                                                                                                                                                          

#     Regular Expression Search Using 'Matches'
#################################################
    if searchOption == "reg-ex":

        searchType = _("Search Type Definition regular expression") + ' - ' + _("Search Type Definition case-sensitive")

        poemSearchLineResults = p.complex_query('\
         declare variable $query := "%s"; \
         declare variable $poem_nodes as node()* := collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg/tei:l; \
         let $start := %s \
         let $end := %s \
         for $x at $i in $poem_nodes[matches(., $query)] \
         return $x[$i = ($start to $end)] \
            ' % (searchStr, int(pageStart), pageEnd))   

        poemSearchLineResultsCount = p.complex_query('\
            declare variable $query := "%s"; \
            declare variable $poem_nodes as node()* := %s; \
            let $total := count($poem_nodes[matches(., $query)]) \
            return $total \
            ' % (searchStr, poem_nodes))                   
           
        poemSearchLineResultsText = ""
        poemSearchLineGroupResultsText = ""
        poemCount = 0
        
        while poemSearchLineResults.hasNext():
            poemSearchLineValues = poemSearchLineResults.next()
            poemSearchLineResultsText += p.process_element(poemSearchLineValues, 'gutorglyn/search_results_reg_ex.py', False, None)
            poemCount += 1
            
        while poemSearchLineResultsCount.hasNext():
            poemSearchLineResultsCountValue = poemSearchLineResultsCount.next()
            poemSearchLineResultsCountNumber = int(poemSearchLineResultsCountValue.asString())
            totalPageNum = math.ceil(float(poemSearchLineResultsCountNumber)/int(perPage))
            
        pageValuesList = []
        for i in range(0, int(totalPageNum) * int(perPage) + 1, int(perPage)):
            pageValuesList.append(i)  
            
        try:
            currentPageNumber = pageValuesList.index(pageEnd)
        except:
            currentPageNumber = '1' 
            
        if poemSearchLineResultsCountNumber < pageEnd:
            pageEnd = poemSearchLineResultsCountNumber                         
              

        return render_to_response('gutorglyn/searchResultsGlobal.html', {     
                                                       'debug': debug_flag, 
                                                       'pageEnd': pageEnd,  
                                                       'pageNumber': currentPageNumber,
                                                       'pageNumberValues': pageValuesList,                                                                     
                                                       'pageStart': pageStart,                                                       
                                                       'perPage': perPage,                                                                                                                          
                                                       'poemSearchGroupHits': poemSearchLineGroupResultsText,
                                                       'searchLineHits': poemSearchLineResultsText,
                                                       'searchMode': searchMode,
                                                       'searchNum': poemSearchLineResultsCountNumber,
                                                       'searchOption': searchOption,                                                        
                                                       'searchTrm': searchStr,
                                                       'searchType': searchType,
                                                       'totalPageNumber': totalPageNum,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                       })              

#     Search Using 'Contains'
############################## 
    else:
        searchLineResultsCount = p.complex_query('\
            declare variable $query := "%s"; \
            declare variable $poem_nodes as node()* := %s; \
            let $total := count($poem_nodes[%s(., $query)]) \
            return $total \
            ' % (smart_str(searchStr), searchModes[searchMode]['xml_nodes'], containsType))                   
            
        query = '\
            declare variable $query := "%s"; \
            declare variable $poem_nodes as node()* := %s; \
            let $total := count($poem_nodes[%s(., $query)]) \
            return $total \
            ' % (smart_str(searchStr), searchModes[searchMode]['xml_nodes'], containsType) 
            
        # get number of pages for search results based on per-page value
        while searchLineResultsCount.hasNext():
            searchLineResultsCountValue = searchLineResultsCount.next()
            searchLineResultsCountNumber = int(searchLineResultsCountValue.asString())
            totalPageNum = math.ceil(float(searchLineResultsCountNumber)/int(perPage))

            
        pageValuesList = []
        for i in range(0, int(totalPageNum) * int(perPage) + 1, int(perPage)):
            pageValuesList.append(i)  
            
        try:
            currentPageNumber = pageValuesList.index(pageEnd)
        except:
            currentPageNumber = '1'                          
                
        if searchMode == 'explanatory_notes':
            searchLineResults = p.complex_query(searchNotesXquery(searchStr, searchModes[searchMode]['xml_nodes'], searchModes[searchMode]['xml_id'], searchModes[searchMode]['xml_title'], containsType, pageEnd, pageStart))
        elif searchMode == 'names':
            searchLineResults = p.complex_query('for $lines in collection("gutorglyn.bdbxml")//tei:div[@type="nodyn_noddwr"]/tei:div[@type="%s"]/tei:p where some $line in $lines satisfies (%s($line, "%s")) return $lines' % (lang, containsType, smart_str(searchStr)))
        elif searchMode == 'text_notes':
            searchLineResults = p.complex_query('for $lines in collection("gutorglyn.bdbxml")//tei:div[@type="Testunol"]/tei:note/tei:p where some $line in $lines satisfies (%s($line, "%s")) return $lines' % (containsType, smart_str(searchStr)))
        else:
            searchLineResults = p.complex_query(searchXquery(searchStr, searchModes[searchMode]['xml_nodes'], searchModes[searchMode]['xml_id'], searchModes[searchMode]['xml_title'], containsType, pageEnd, pageStart))                                                                                                                                                                                                    
                  
        while searchLineResults.hasNext():
            searchLineValues = searchLineResults.next()
            searchLineResultsText += p.process_element(searchLineValues, searchModes[searchMode]['pixelate'], False, None)
            count += 1          

        if searchLineResultsCountNumber < pageEnd:
            pageEnd = searchLineResultsCountNumber
        
        return render_to_response(resultsTemplate, {'containsType': containsType,
                                                                   'debug': debug_flag,                                                                   
                                                                   'pageStart': pageStart,
                                                                   'pageEnd': pageEnd,                                                                                                                      
                                                                   'perPage': perPage,
                                                                   'pageNumber': currentPageNumber,
                                                                   'pageNumberValues': pageValuesList,
                                                                   'searchLineHits': searchLineResultsText,
                                                                   'searchMode': searchMode,                                                                      
                                                                   'searchNum': searchLineResultsCountNumber, 
                                                                   'searchOption': searchOption,                                                                         
                                                                   'searchTrm': searchStr,                                                                                                                                                                                                                                                                                                                                                              
                                                                   'searchType': searchType,
                                                                   'totalPageNumber': totalPageNum,                                                                                                                                                                    
                                                                   })
        
               


def searchStart(request):
    searchTerm = request.GET.get('searchVal', '')
    return render_to_response('gutorglyn/search-start.html',{'searchTerm': searchTerm})    

def searchTest (request):
    searchStr = request.GET.get('searchVal', '')
    matchCaseFlag = request.GET.get('match-case', '')
    searchLineResultsText = ""
    pageStart = request.GET.get('page-start', '')
    perPage = request.GET.get('per-page', '')
    pageEnd = 18
    
    p = Collection(request, 'gutorglyn') 
       
#     XML Paths for Xquery function
    explanatory_notes_nodes = 'collection("gutorglyn.bdbxml")//tei:div[@type="Esboniadol"]/tei:note'
    explanatory_notes_xml_id = '/../@xml:id'
    explanatory_notes_title = '/../../tei:head'
    paraphrases_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[2]/tei:lg'
    paraphrases_xml_id = '/../@xml:id'
    paraphrases_title = '/../../tei:head'
    poem_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg'
    poem_xml_id = '/../@xml:id'
    poem_title = '/../../tei:head'    
    sources_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[7]/tei:div[1]/tei:div[1]/tei:lg'
    sources_xml_id = '/../../../../@xml:id'
    sources_title = '/../tei:head'
    translations_nodes = 'collection("gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[3]/tei:lg'
    translations_xml_id = '/../@xml:id'
    translations_title = '/../../tei:head'
    
    if matchCaseFlag == "off":
        containsType = "dbxml:contains"
    else:
        containsType = "contains"    
    
    searchLineResults = p.complex_query(searchNotesXquery(searchStr, explanatory_notes_nodes, explanatory_notes_xml_id, explanatory_notes_title, containsType, pageEnd, pageStart))
        
    while searchLineResults.hasNext():
        searchLineValues = searchLineResults.next()
        searchLineResultsText += p.process_element(searchLineValues, 'gutorglyn/search_results_explanatory_notes.py', False, None)  
            
    return render_to_response('gutorglyn/xquery-test.html', {
                                                               'searchLineHits': searchLineResultsText,
                                                               'containsType': containsType,
                                                               'query': searchLineResults,                                                                                                                                                                               
                                                               })       
       
def searchXquery(searchStr=None, nodes=None, xml_id=None, title=None, containsType=None, pageEnd=None, pageStart=None):
    
    xquery = ' \
        declare variable $query := "%s"; \
        declare variable $user_doc as node()* := %s; \
         \
        declare function local:remove-elements($input as element()*) as element() {  \
           element {node-name($input) } \
              {$input/@*, \
              attribute xml:id {$input%s}, \
              attribute title {$input%s}, \
               for $child in $input/node() \
                  return \
                    if ($child[%s((.),$query)]) \
                    then ( \
                        if ($child/preceding-sibling::*[3][%s((.),$query)]) \
                            then ( \
                            ) \
                        else ( \
                            if ($child/preceding-sibling::*[2][%s((.),$query)]) \
                                then ( \
                                ) \
                                else ( \
                                    $child/preceding-sibling::*[2] \
                                ) \
                        ), \
                        if ($child/preceding-sibling::*[2][%s((.),$query)]) \
                            then ( \
                            ) \
                        else ( \
                            if ($child/preceding-sibling::*[1][%s((.),$query)]) \
                                then ( \
                               ) \
                            else ( \
                               $child/preceding-sibling::*[1] \
                           ) \
                        ), \
                        $child, \
                        if ($child/following-sibling::*[1][%s((.),$query)]) \
                            then ( \
                           ) \
                        else ( \
                            $child/following-sibling::*[1] \
                            ), \
                       if ($child/following-sibling::*[3][%s((.),$query)]) \
                           then ( \
                           ) \
                       else ( \
                            if ($child/following-sibling::*[2][%s((.),$query)]) \
                               then ( \
                               ) \
                            else ( \
                               $child/following-sibling::*[2] \
                               ) \
                            ) \
                        ) \
                    else () \
              } \
        }; \
         \
        let $end := %s \
        let $start := %s \
        let $results := \
        for $i in (1 to count($user_doc)) \
        return \
            if (%s($user_doc[$i], $query)) \
            then \
            (local:remove-elements($user_doc[$i])) \
            else () \
        return $results[position() = ($start to $end)]\
        ' % (smart_str(searchStr), nodes, xml_id, title, containsType, containsType, containsType, containsType, containsType, containsType, containsType, containsType, int(pageEnd), int(pageStart), containsType)
    
    return xquery

def searchNotesXquery(searchStr=None, nodes=None, xml_id=None, title=None, containsType=None, perPage=None, pageStart=None):    
    xquery = ' \
        declare variable $query := "%s"; \
        declare variable $user_doc as node()* := %s; \
         \
        declare function local:remove-elements($input as element()*) as element() {  \
           element {node-name($input) } \
              {$input/@*, \
              attribute xml:id {$input%s}, \
              attribute title {$input%s}, \
               for $child in $input/node() \
                  return \
                    if ($child[%s((.),$query)]) \
                    then ( \
                        $child \
                        ) \
                    else () \
              } \
        }; \
         \
        let $perpage := %s \
        let $start := %s \
        let $end := $start + $perpage \
        let $results := \
        for $i in (1 to count($user_doc)) \
        return \
            if (%s($user_doc[$i], $query)) \
            then \
            (local:remove-elements($user_doc[$i])) \
            else () \
        return $results[position() = ($start to $end)]\
        ' % (smart_str(searchStr), nodes, xml_id, title, containsType, int(perPage), int(pageStart), containsType)
    
    return xquery

def service(request, t=None):
    view = request.GET.get('v', '')
    poem = request.GET.get('p', '')
    lang = request.GET.get('lang', '')    
    
    url = 'gutorglyn/services/service.html'
    
    p = Collection(request, 'gutorglyn')
    
    query           =   ''
    errorMessage    =   ''
    editedText      =   ''
    paraphrase      =   ''
    translation     =   ''
    titleCy         =   ''
    titleEn         =   ''    
    textNotes       =   ''
    exNotes         =   ''
    exEngNotes      =   ''
    patron          =   ''
    editor          =   ''
    
    editedTextQuery     =   '//tei:div[@xml:id="Guto%stestun"]' % (poem)
    paraphraseQuery     =   '//tei:div[@xml:id="Guto%saralleiriad"]' % (poem)
    translationQuery    =   '//tei:div[@xml:id="Guto%stranslation"]' % (poem)
    titleCyQuery        =   '//tei:div[@xml:id="Guto%stop"]/tei:head' % (poem)
    titleEnQuery        =   '//tei:div[@xml:id="Guto%stop"]/tei:div[3]/tei:lg[1]/tei:l[1]' % (poem)    
    textNotesQuery      =   '//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Testunol"]' % (poem)
    exNotesQuery        =   '//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Esboniadol"]' % (poem) 
    exEngNotesQuery     =   '//tei:div[@xml:id="Guto%stop"]/tei:div[@type="Explanatory"]' % (poem)
    patronQuery         =   '//tei:div/tei:div[@xml:id="Guto%sexplanatory"]/tei:note/tei:p/tei:name' % (poem)
    editorQuery         =   '//tei:div[@xml:id="Guto%stop"]/tei:note[@type="golygydd"]' % (poem)   
    
    if view == 'editedText':
        query = p.query(editedTextQuery)
        errorMessage = 'Cannot find editedText'
        
        if query.hasNext():
            queryValues = query.next()
        else:
            return render_to_response(errorURL, {'message': errorMessage})
        editedText = p.process_element(queryValues, servicePixelateURL, False, None)
        
    elif view == 'paraphrase':
        query = p.query(paraphraseQuery)
        errorMessage = 'Cannot find paraphrase'
        
        if query.hasNext():
            queryValues = query.next()
        else:
            return render_to_response(errorURL, {'message': errorMessage})
        paraphrase = p.process_element(queryValues, servicePixelateURL, False, None)       

    elif view == 'translation':
        query = p.query(translationQuery)
        errorMessage = 'Cannot find translation'
        
        if query.hasNext():
            queryValues = query.next()
        else:
            return render_to_response(errorURL, {'message': errorMessage})
        translation = p.process_element(queryValues, servicePixelateURL, False, None)         

    elif view == 'titleCy':
        query = p.query(titleCyQuery)
        errorMessage = 'Cannnot find Cymraeg Title'
        
        if query.hasNext():
            queryValues = query.next()
        else:
            return render_to_response(errorURL, {'message': errorMessage})
        titleCy = p.process_element(queryValues, servicePixelateURL, False, None)
        
    elif view == 'titleEn':
        query = p.query(titleEnQuery)
        errorMessage = 'Cannnot find English Title'
        
        if query.hasNext():
            queryValues = query.next()
        else:
            return render_to_response(errorURL, {'message': errorMessage})
        titleEn = p.process_element(queryValues, servicePixelateURL, False, None)        
   

    elif view == 'textNotes':
        query = p.query(textNotesQuery)
        errorMessage = 'Cannnot find text notes'
        
        if query.hasNext():
            queryValues = query.next()
        else:
            return render_to_response(errorURL, {'message': errorMessage})
        textNotes = p.process_element(queryValues, servicePixelateURL, False, None)

    elif view == 'exNotes':
        query = p.query(exNotesQuery)
        errorMessage = 'Cannot find Explanatory Notes'
        
        if query.hasNext():
            queryValues = query.next()
        else:
            return render_to_response(errorURL, {'message': errorMessage})
        exNotes = p.process_element(queryValues, servicePixelateURL, False, None)
    
    elif view == 'exEngNotes':
        query = p.query(exEngNotesQuery)
        errorMessage = 'Cannot find English Explanatory Notes'
        
        if query.hasNext():
            queryValues = query.next()
        else:
            return render_to_response(errorURL, {'message': errorMessage})
        exEngNotes = p.process_element(queryValues, servicePixelateURL, False, None)
    
    elif view == 'editor':
        query = p.query(editorQuery)
        errorMessage = 'Cannot find editor'
        
        if query.hasNext():
            queryValues = query.next()
        else:
            return render_to_response(errorURL, {'message': errorMessage})
        editor = p.process_element(queryValues, servicePixelateURL, False, None)        
         
    elif view == 'patron':
        query = p.query(patronQuery)
        errorMessage = 'Cannot find patron'
                
        if query.hasNext():
            queryValues = query.next()
        else:
            return render_to_response(errorURL, {'message': errorMessage})
        patron = p.process_element(queryValues, servicePixelateURL, False, None)    
                                           
    else:
        errorMessage = '<h1 style="color:red">Warning</h1><p>Function Not found: <strong>%s</strong></p>' % (view)
        return HttpResponse(errorMessage, status=404)
        
    return render_to_response(url, {'editedText': editedText,
                                    'paraphrase': paraphrase,
                                    'translation': translation,
                                    'titleCy': titleCy,
                                    'titleEn': titleEn,
                                    'textNotes': textNotes,
                                    'exNotes': exNotes,
                                    'exEngNotes': exEngNotes,
                                    'patron': patron,
                                    'editor': editor
                                    })  

def titleList(request):
    return render_to_response('gutorglyn/title-list.html',)

def titleListCy(request):
    return render_to_response('gutorglyn/titles-cy.txt',)    

def titleListEn(request):
    return render_to_response('gutorglyn/titles-en.txt',)        

def generateTitleDropdown(request):

    
    cyTitleQuery = "declare variable $poemOrderSequence := %s; " % str(poemOrderSequence)    
    cyTitleQuery = cyTitleQuery +"declare variable $ggg := collection('gutorglyn/gutorglyn.bdbxml')//tei:div[@type='lev0']; "
    cyTitleQuery = cyTitleQuery + "<select id='poem' name='poem'><option value='#'>Dewis...</option> "
    cyTitleQuery = cyTitleQuery + "{ for $titleNumber in $poemOrderSequence "
    cyTitleQuery = cyTitleQuery + "return "        
    cyTitleQuery = cyTitleQuery + "for $v in $ggg "
    cyTitleQuery = cyTitleQuery + "let $w := substring-after($v/@xml:id, 'Guto') "
    cyTitleQuery = cyTitleQuery + "let $x := substring-before($w, 'top') "
    cyTitleQuery = cyTitleQuery + "let $y := $v/tei:head/text() "
    cyTitleQuery = cyTitleQuery + "where $x = $titleNumber "                
    cyTitleQuery = cyTitleQuery + "return "                
    cyTitleQuery = cyTitleQuery + "<option value='{$x}'>"
    cyTitleQuery = cyTitleQuery + "{$y}"
    cyTitleQuery = cyTitleQuery + "</option>"
    cyTitleQuery = cyTitleQuery + "}</select>"    
        
    enTitleQuery = "declare variable $poemOrderSequence := %s; " % str(poemOrderSequence)
    enTitleQuery = enTitleQuery +"declare variable $ggg := collection('gutorglyn/gutorglyn.bdbxml')//tei:div[@type='lev2'][2]; "
    enTitleQuery = enTitleQuery + "<select id='poem' name='poem'><option value='#'>Choose...</option> "
    enTitleQuery = enTitleQuery + "{ for $titleNumber in $poemOrderSequence "
    enTitleQuery = enTitleQuery + "return "
    enTitleQuery = enTitleQuery + "for $v in $ggg "
    enTitleQuery = enTitleQuery + "let $w := substring-after($v/@xml:id, 'Guto') "
    enTitleQuery = enTitleQuery + "let $x := substring-before($w, 'translation') "
    enTitleQuery = enTitleQuery + "let $y := $v/tei:lg[1]/tei:l[1]/descendant-or-self::text() "
    enTitleQuery = enTitleQuery + "where $x = $titleNumber "
    enTitleQuery = enTitleQuery + "return "
    enTitleQuery = enTitleQuery + "<option value='{$x}'>"
    enTitleQuery = enTitleQuery + "{$y}"
    enTitleQuery = enTitleQuery + "</option>"
    enTitleQuery = enTitleQuery + "}</select>"            

    xmlMgr = XmlManager()
    
    myContainer = xmlMgr.openContainer("gutorglyn/gutorglyn.bdbxml")
    qcontext = xmlMgr.createQueryContext()
    qcontext.setDefaultCollection("gutorglyn/gutorglyn.bdbxml")
    qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")
    

    queryexp = xmlMgr.prepare(cyTitleQuery, qcontext)
    
    results = queryexp.execute(qcontext)
    
    for value in results:
        document = value.asDocument()
        name = document.getName()
        cyContent = value.asString()
        
    queryexp = xmlMgr.prepare(enTitleQuery, qcontext)
    
    results = queryexp.execute(qcontext)
    
    for value in results:
        document = value.asDocument()
        name = document.getName()
        enContent = value.asString()
                
    
    del myContainer    
    
#     return render_to_response('gutorglyn/title-list2.html', {'titleList': content,})  
    f = open('gutorglyn/templates/gutorglyn/titles-cy.txt', 'w')
    f.write(cyContent)
    f.close()
    
    f = open('gutorglyn/templates/gutorglyn/titles-en.txt', 'w')
    f.write(enContent)
    f.close()    
    
    message = '<h1>Gwaith Guto\'r Glyn Maintenence</h1><hr/><h2>Title Dropdown Menus have been refreshed!</h2>'
    
    return HttpResponse(message, content_type="text/html")

def transcripts(request):
    
    lang = request.COOKIES.get('gutorglynlang', '')
    lang = getLang(lang)    
    
    try:
        transcript = request.GET.get('transcript', '')
        
    except:        
        transcript = request.COOKIES.get('gutorglynTranscript', '')
        
    transcriptVal = str(transcript)
    
    try:
        poemVal = request.GET.get('poem', '')
        
    except:
        poemVal = request.COOKIES.get('gutorglynpoem')
    
    transcriptIndex = request.GET.get('index', '')
    
    p = Collection(request, 'gutorglyn')
    
    firstTranscriptVal = ''
    
    if transcriptVal == '':
        firstTranscriptVal = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="llawysgrifau"]/tei:div[1]/@xml:id' % (poemVal))
        
        if firstTranscriptVal.hasNext():
            firstTranscriptValText = firstTranscriptVal.next()
        
        titleSeperator = '"'
        firstTransTitle = firstTranscriptValText.asString()
        firstTransTitleVal = firstTransTitle.split(titleSeperator,1)[1]
        firstTransTitleVal = firstTransTitleVal.split(titleSeperator,1)[0]
        
        transcriptVal = firstTransTitleVal
    
    else:
        
        transcriptVal = str(transcript)
               
    transcriptText = p.query('//tei:div[@xml:id="%s"]/tei:div' % (transcriptVal))
    transcriptTitle = p.query('//tei:div[@xml:id="%s"]/tei:div/tei:head' % (transcriptVal))      
    transcriptTitles = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="llawysgrifau"]/tei:div/tei:div/tei:head' % (poemVal))
    transcriptLineNums = p.query('//tei:div[@xml:id="%s"]/tei:div[@type="nodiadau"]/tei:div[@type="%s"]/tei:note[@type="trefn_%s"]' % (transcriptVal, lang, lang))
    transcriptHand = p.query('//tei:div[@xml:id="%s"]/tei:div[@type="nodiadau"]/tei:div[@type="%s"]/tei:note[@type="llaw_%s"]' % (transcriptVal, lang, lang))
    transcriptDate = p.query('//tei:div[@xml:id="%s"]/tei:div[@type="nodiadau"]/tei:div[@type="%s"]/tei:note[@type="dyddiad_%s"]' % (transcriptVal, lang, lang))
    transcriptNotes = p.query('//tei:div[@xml:id="%s"]/tei:div[@type="nodiadau"]/tei:div[@type="%s"]/tei:note[@type="nodiadau_trawsysgrifiad_%s"]' % (transcriptVal, lang, lang))

    if transcriptText.hasNext():
        transcriptTextValues = transcriptText.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription text"})
    transcriptText = p.process_element(transcriptTextValues, 'gutorglyn/variant.py', False, None)   
    
    if transcriptTitle.hasNext():
        transcriptTitleValue = transcriptTitle.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription title"})
    transcriptTitleText = p.process_element(transcriptTitleValue, 'gutorglyn/variant-title.py', False, None)    
    
    if transcriptLineNums.hasNext():
        transcriptLineNumsValues = transcriptLineNums.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription line numbers"})
    transcriptLineNumsText = p.process_element(transcriptLineNumsValues, 'gutorglyn/variant.py', False, None)  
    
    if transcriptHand.hasNext():
        transcriptHandValues = transcriptHand.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription hand"})
    transcriptHandText = p.process_element(transcriptHandValues, 'gutorglyn/variant.py', False, None)
    
    if transcriptDate.hasNext():
        transcriptDateValues = transcriptDate.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription date"})
    transcriptDateText = p.process_element(transcriptDateValues, 'gutorglyn/variant.py', False, None)   
    
    transcriptNotesText = ""
    while transcriptNotes.hasNext():
        thistranscriptNote = transcriptNotes.next()
        transcriptNotesText += p.process_element(thistranscriptNote, 'gutorglyn/variant.py', False, None)                            
        
    transcriptTitlesText = ""
        
    while transcriptTitles.hasNext():
        thisTranscriptTitle = transcriptTitles.next()
        transcriptTitlesText += p.process_element(thisTranscriptTitle, 'gutorglyn/variant-titles-select.py', False, None)    

    return render_to_response('gutorglyn/transcripts.html', {'transcriptText': transcriptText,
                                                             'transcriptTitle': transcriptTitleText,
                                                             'transcriptLineNumsText': transcriptLineNumsText,
                                                             'transcriptHandText': transcriptHandText,
                                                             'transcriptDateText': transcriptDateText,
                                                             'transcriptNotesText': transcriptNotesText,
                                                             'transcriptTitles': transcriptTitlesText,
                                                             'poemNum': poemVal,
                                                             'transcriptIndex': transcriptIndex,
                                                             'transcriptID': transcriptVal,
                                                             })

def transcriptImage(request):

    lang = request.COOKIES.get('gutorglynlang', '')
    lang = getLang(lang)      
    
    poemVal = request.GET.get(r'poem', '')
    
    try:
        transcript = request.GET.get('transcript', '')        
    except:        
        transcript = request.COOKIES.get('gutorglynTranscript', '')        
        
    transcriptVal = str(transcript)
    transcriptIndex = request.GET.get('index', '')
    
    p = Collection(request, 'gutorglyn')
    
    if transcriptVal == '':        
        transcriptImageIDLocation1 = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="llawysgrifau"]/tei:div[1]/tei:div/tei:pb[1]' % (poemVal))
    elif transcriptIndex == '':
        transcriptImageIDLocation1 = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="llawysgrifau"]/tei:div[@xml:id="%s"]/tei:div/tei:pb[1]' % (poemVal,transcriptVal))        
    else:
        transcriptImageIDLocation1 = p.query('//tei:div[@xml:id="%s"]/tei:div/tei:pb[@n="%s"]' % (transcriptVal, transcriptIndex))
        transcriptImageIDLocation2 = p.query('//tei:div[@xml:id="%s"]/tei:div/tei:lg/tei:pb[@n="%s"]' % (transcriptVal, transcriptIndex))            
        
    if transcriptImageIDLocation1.hasNext():
        transcriptImageIDValues = transcriptImageIDLocation1.next()
    elif transcriptImageIDLocation2.hasNext():
        transcriptImageIDValues = transcriptImageIDLocation2.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription ID: " + transcriptIndex})
    transcriptImageIDText = p.process_element(transcriptImageIDValues, 'gutorglyn/variant-image.py', False, None)   

    return render_to_response('gutorglyn/transcript-image.html', {
                                                            'transcriptImageID': transcriptImageIDText,                                                            
                                                             })

def transcriptImages(request):

    lang = request.COOKIES.get('gutorglynlang', '')
    lang = getLang(lang)      
    
    try:
        transcript = request.GET.get('transcript', '')        
    except:        
        transcript = request.COOKIES.get('gutorglynTranscript', '')
        
    transcriptVal = str(transcript)
    
    poemVal = request.GET.get('poem', '')    
    transcriptIndex = request.GET.get('index', '')
    role = request.GET.get('role', '')
    
    pixelate = ''
    if role == '':
        pixelate = 'transcript-images.html'
    else:
        pixelate = 'transcript-images-viewer.html'
    
    p = Collection(request, 'gutorglyn')
    
    firstTranscriptValText = ''
    
    if transcriptVal == '':
        firstTranscriptVal = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="llawysgrifau"]/tei:div[1]/@xml:id' % (poemVal))
        
        if firstTranscriptVal.hasNext():
            firstTranscriptValText = firstTranscriptVal.next()
        
        titleSeperator = '"'
        firstTransTitle = firstTranscriptValText.asString()
        firstTransTitleVal = firstTransTitle.split(titleSeperator,1)[1]
        firstTransTitleVal = firstTransTitleVal.split(titleSeperator,1)[0]
        
        transcriptVal = firstTransTitleVal
    
    else:
        
        transcriptVal = str(transcript)
               
    transcriptText = p.query('//tei:div[@xml:id="%s"]/tei:div' % (transcriptVal))
    transcriptTitle = p.query('//tei:div[@xml:id="%s"]/tei:div/tei:head' % (transcriptVal))      
    transcriptTitles = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="llawysgrifau"]/tei:div/tei:div/tei:head' % (poemVal))
    transcriptLineNums = p.query('//tei:div[@xml:id="%s"]/tei:div[@type="nodiadau"]/tei:div[@type="%s"]/tei:note[@type="trefn_%s"]' % (transcriptVal, lang, lang))
    transcriptHand = p.query('//tei:div[@xml:id="%s"]/tei:div[@type="nodiadau"]/tei:div[@type="%s"]/tei:note[@type="llaw_%s"]' % (transcriptVal, lang, lang))
    transcriptDate = p.query('//tei:div[@xml:id="%s"]/tei:div[@type="nodiadau"]/tei:div[@type="%s"]/tei:note[@type="dyddiad_%s"]' % (transcriptVal, lang, lang))
    transcriptNotes = p.query('//tei:div[@xml:id="%s"]/tei:div[@type="nodiadau"]/tei:div[@type="%s"]/tei:note[@type="nodiadau_trawsysgrifiad_%s"]' % (transcriptVal, lang, lang))

    if transcriptText.hasNext():
        transcriptTextValues = transcriptText.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription text"})
    transcriptText = p.process_element(transcriptTextValues, 'gutorglyn/variant-images.py', False, None)   
    
    if transcriptTitle.hasNext():
        transcriptTitleValue = transcriptTitle.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription title"})
    transcriptTitleText = p.process_element(transcriptTitleValue, 'gutorglyn/variant-title.py', False, None)    
    
    if transcriptLineNums.hasNext():
        transcriptLineNumsValues = transcriptLineNums.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription line numbers"})
    transcriptLineNumsText = p.process_element(transcriptLineNumsValues, 'gutorglyn/variant-images.py', False, None)  
    
    if transcriptHand.hasNext():
        transcriptHandValues = transcriptHand.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription hand"})
    transcriptHandText = p.process_element(transcriptHandValues, 'gutorglyn/variant-images.py', False, None)
    
    if transcriptDate.hasNext():
        transcriptDateValues = transcriptDate.next()
    else:
        return render_to_response('gutorglyn/error.html', {'message': "Can't find transcription date"})
    transcriptDateText = p.process_element(transcriptDateValues, 'gutorglyn/variant-images.py', False, None)   
    
    transcriptNotesText = ""
    while transcriptNotes.hasNext():
        thisTranscriptNote = transcriptNotes.next()
        transcriptNotesText += p.process_element(thisTranscriptNote, 'gutorglyn/variant-images.py', False, None)                            
        
    transcriptTitlesText = ""
        
    while transcriptTitles.hasNext():
        thisTranscriptTitle = transcriptTitles.next()
        transcriptTitlesText += p.process_element(thisTranscriptTitle, 'gutorglyn/variant-titles-select.py', False, None)    

    return render_to_response('gutorglyn/'+str(pixelate), {
                                                            'poemNum': poemVal,     
                                                            'transcriptText': transcriptText,
                                                            'transcriptTitle': transcriptTitleText,
                                                            'transcriptLineNumsText': transcriptLineNumsText,
                                                            'transcriptHandText': transcriptHandText,
                                                            'transcriptDateText': transcriptDateText,
                                                            'transcriptNotesText': transcriptNotesText,
                                                            'transcriptTitles': transcriptTitlesText,                                                             
                                                            'transcriptIndex': transcriptIndex,
                                                            'transcriptID': transcriptVal,                                                            
                                                             })

def tuchwith(request):                    
    return render_to_response('gutorglyn/tuchwith.html',)

def variantLines(request):
    
    poem = request.GET.get(r'p', '')
    line = request.GET.get(r'l', '')     
    
    p = Collection(request, 'gutorglyn')
    variantLineValues = p.query('//tei:div[@xml:id="Guto%stop"]/tei:div[@type="llawysgrifau"]/tei:div/tei:div/tei:lg/tei:l[@n="%s"]' % (poem,line))
    
    variantLinesText = ""
    
    while variantLineValues.hasNext():
        thisVariantLine = variantLineValues.next()
        variantLinesText += p.process_element(thisVariantLine, 'gutorglyn/variant-lines.py', False, None)
    
    return render_to_response('gutorglyn/variant-lines.html', {'variantLines': variantLinesText})
   




       