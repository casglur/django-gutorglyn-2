"""Create your XML Element Processors here."""

import inspect

PIXELISE_PATTERNS = {
    'a':'a',                     
    '//body/div':'noteDiv',                 
    'div/head':'head',
    'figure':'figure',
    '//figure/head':'imgHead',
    'hi':'hi',  
    'lb':'lb',   
    'name':'name',       
    'p':'p',
}

def a(element, context,args):
    href = element.get_attribute_value('href')  
    if context=="begin":             
            html='<a href="%s">' % href
            return html                       
    
    if context=="end":              
            html='</a>' 
            return html    

def figure(element, context, args):
    graphicType = element.get_attribute_value('type')    
    graphicNode = element.get_child('graphic')
    graphicNodeSrc = graphicNode.get_attribute_value('url')
    
    graphicDir = None
    if graphicType == 'llun':
        graphicDir = 'photos'
    if graphicType == 'ach':
        graphicDir = 'lineage'
    if graphicType == 'stema':
        graphicDir = 'stemma'
    
    if context=="begin":        
        html='<p><a href="/static/img/%s/%s" target="_blank"><img style="border-style:solid; border-color: #DBE3C0 #3D3D3D #3D3D3D #DBE3C0;width:200px;" alt="lineage" src="/static/img/%s/%s"/></a><br/>' % (graphicDir,graphicNodeSrc,graphicDir,graphicNodeSrc)
        return html
    if context=="end":              
        html='</p>' 
        return html
    
def head(element, context,args):
    previousDiv = element.get_parent_element()
    nameDiv = previousDiv.get_parent_element()
    nameId = nameDiv.get_attribute_value('xml:id')
    if context=="begin":
        html ='<a id="%s"><h3 class="title">' % nameId
        return html
    if context=="end":
        html = '</h3></a><a href="#top">Top</a>'
        return html     

def hi(element, context, args):
    rend = element.get_attribute_value('rend')
    if context=="begin":             
        if rend=='bold':
            html='<b>' 
            return html        
        elif rend=='italics':
            html='<i>'
            return html
        elif rend=='quote':
            html='<blockquote>'
            return html            
        elif rend=='subscript':
            html='<sub>'
            return html             
        elif rend=='superscript':
            html='<sup>'
            return html            
    
    if context=="end":              
        if rend=='bold':
            html='</b>' 
            return html         
        elif rend=='italics':
            html='</i>'
            return html
        elif rend=='quote':
            html='</blockquote>'
            return html             
        elif rend=='subscript':
            html='</sub>'
            return html             
        elif rend=='superscript':
            html='</sup>'
            return html  

def imgHead(element, context, args):
    if context=="begin":
        html ='<i>'
        return html
    if context=="end":
        html = '</i>'
        return html

def lb(element, context, args):
    if context =="begin":
        html = '<br/>'
        return html 

def name(element, context, args):    
    nameVal = element.get_attribute_value('ref')
    nameType = element.get_attribute_value('type')    
    parentElement = element.get_parent_element()    
    
    parentElementName = parentElement.get_node_name()
    
    location = ''
    if parentElementName=="p":
        if nameType=="noddwr": 
            location='javascript:popUp(\'/gutorglyn/name/?n=%s\')' % (nameVal)
        if nameType=="lle":
            location='javascript:popUp(\'/gutorglyn/name/?n=%s\')' % (nameVal)
        if nameType=="pobl":
            location='javascript:popUp(\'/gutorglyn/name/?n=%s\')' % (nameVal)
    else:
        if nameType=="noddwyr":
            location='javascript:popUp(\'//www.dafyddapgwilym.net/ggg/personGetCym.php?personID=%s\')' % (nameVal)
        if nameType=="pobl": 
            location='javascript:popUp(\'//www.dafyddapgwilym.net/ggg/personGetCym.php?personID=%s\')' % (nameVal)
        if nameType=="lle":
            location='javascript:popUp(\'//www.dafyddapgwilym.net/ggg/placeGetCym.php?placeID=%s\')' % (nameVal)    

    if context=="begin":
            html='<a class="name" href="%s">' % (location)
            return html
    if context=="end":              
        html='</a>' 
        return html
    
def noteDiv(element,context,args):
    nameId = element.get_attribute_value('xml:id')
    nameDiv = element.get_child('div')
    nameHead = nameDiv.get_child('head')
    if context=="begin":
        html ='<a href="#%s">%s' % (nameId,nameHead)
        return html
    if context=="end":
        html = '</a><br/>'
        return html
    if context=="content":
        return {'hide_content':True}     

def p(element, context, args):
    html=""
    try:
        rend = element.get_attribute_value('rend')
    except:
        if context=="begin":
            html = '<p>'
        if context=="end":
            html = '</p>'
    else:
        if context=="begin":
            if rend=='centre':
                html='<p align="center">'
        else:
            html = '<p class="%s">' % (rend)
        if context=="end":
            html = '</p>'
    return html

 
        