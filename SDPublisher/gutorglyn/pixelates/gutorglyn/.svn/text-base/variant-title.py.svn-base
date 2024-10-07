"""Create your XML Element Processors here."""

import inspect


PIXELISE_PATTERNS = {
    'div/head': 'head',
}

def head(element, context,args):
    if context=="begin":
        html ='<div id="transcript-title">'
        return html
    if context=="end":
        html = '</div>'
        return html
        
