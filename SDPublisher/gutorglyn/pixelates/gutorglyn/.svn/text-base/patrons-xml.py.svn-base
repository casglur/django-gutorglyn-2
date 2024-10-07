"""Create your XML Element Processors here."""

import inspect

PIXELISE_PATTERNS = {
    'patrons': 'patrons',
    'patron': 'patron',
    'id': 'id',
    'name': 'name',
}

    
def patrons(element, context,args):
    if context=="begin":
        html ='<patrons>'
        return html
    if context=="end":
        html = '</patrons>'
        return html
        
def patron(element, context,args):
    if context=="begin":
        html ='<patron>'
        return html
    if context=="end":
        html = '</patron>'
        return html
    
def id(element, context,args):
    if context=="begin":
        html ='<id>'
        return html
    if context=="end":
        html = '</id>'
        return html

def name(element, context,args):
    if context=="begin":
        html ='<name>'
        return html
    if context=="end":
        html = '</name>'
        return html        