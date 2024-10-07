# Create your views here.

from pixelise.core import Collection
from django.shortcuts import render_to_response

def text(request):
     global p
     p = Collection(request, 'gutorglynn')
     results = p.query("//text")
     if results.hasNext():
         text = results.next()
     else:
         return render_to_response('gutorglynn/error.html', {'message': "Can't find text element"})
     text_content = p.process_element(text, 'gutorglynn/base.py', False, None)
     return render_to_response('gutorglynn/text.html', {'page_content': text_content})
 
def poem(request):
     global p
     p = Collection(request, 'gutorglynn')
     results = p.query('//div')
     if results.hasNext():
         text = results.next()
     else:
         return render_to_response('gutorglynn/error.html', {'message': "Can't find poem"})
     text_content = p.process_element(text, 'gutorglynn/base.py', False, None)
     return render_to_response('gutorglynn/text.html', {'page_content': text_content})
 
def editedText(request):
     global p
     p = Collection(request, 'gutorglynn')
     results = p.query('//div[@xml:id="Guto08testun"]')
     if results.hasNext():
         text = results.next()
     else:
         return render_to_response('gutorglynn/error.html', {'message': "Can't find poem"})
     text_content = p.process_element(text, 'gutorglynn/base.py', False, None)
     return render_to_response('gutorglynn/text.html', {'page_content': text_content})
