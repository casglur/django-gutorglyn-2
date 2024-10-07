#create your views here

from pixelise.core import Collection
from django.shortcuts import render_to_response

def text(request):
     p = Collection(request, 'origin')
     results = p.query("//text")
     if results.hasNext():
         text = results.next()
     else:
         return render_to_response('origin/error.html', {'message': "Can't find text element"})
     text_content = p.process_element(text, 'origin/base.py', False, None)
     return render_to_response('origin/text.html', {'page_content': text_content})

def chapter(request, chapter=None):
    print "%s" % (chapter)
    p = Collection(request, 'origin')
    results = p.query("//div[@n='CH%s']" % (str(chapter)))
    if results.hasNext():
        text = results.next()
    else:
        return render_to_response('origin/error.html', {'message': "Can't find chapter %s" % (str(chapter))})
    the_content = p.process_element(text, 'origin/base.py', False, None)
    return render_to_response('origin/text.html', {'page_content': the_content})

def page(request, page=None):
    p = Collection(request, 'origin')
    #Grab all the page breaks
    pbn, page, pb = getAllPages(p, page)
    print 'pages found %s' % (len(pbn))
    if pbn == False or page == None:
        return render_to_response('origin/error.html', {'message': "Can't find page %s" % (str(page))})
    else:
        page_content = p.process_element(pb, 'origin/base.py', True, None)
    #Work out the next and previous pages
    thispb = pbn.index(page)
    if thispb == 0:
        previouspb = None
    else:
        previouspb = pbn[thispb - 1]
    if thispb + 1 == len(pbn):
        nextpb = None
    else:
        nextpb = pbn[thispb + 1]
    return render_to_response('origin/text.html', {'page_content': page_content, 'current_p': page, 'previouspb': previouspb, 'nextpb': nextpb})

def getAllPages(p, page):
     #Grab all the page breaks
     results = p.query("//pb")
     if results == None:
         return (False, False, False)
     pbn = []
     while results.hasNext():
         if results.next().get_attribute_value('id')[0] == 'S':
             pbn.append(results.next().get_attribute_value('n'))
     #Grab the pb
     pb = None
     page = str(page)
     results = p.query("//pb[@n='%s']" % page, 1, 1)
     if results.hasNext():
         pb = results.next()
     else:
         page = None
     return (pbn, page, pb) 
 
 
