"""Create your XML Element Processors here."""

import inspect


PIXELISE_PATTERNS = {
    'div': 'div',
    'p': 'p',
    'div/head': 'head',
    'lg': 'lg',
    'l': 'l',
    'lb': 'lb',
    'hi': 'hi',
    'add': 'add',
    'del': 'delete',
    'unclear':'unclear',
    'note':'note',
    'list':'list',
    'item':'item',
}

def div(element, context, args):
    html = ""
    try:
        type = element.get_attribute_value('type')
    except:
        if context == "begin":
            html = ''
            return html
        if context == "end":
            html = ''
            return html        
    else: 
        if context == 'begin':              
            if type == "lev3":
                html = "<div class='transcription'>"
                return html
            if type=='nodiadau':
                html = "<div class='notes'>"
                return html
            if type=='cym':
                html="<div class='cym-notes'>"
                return html
            if type=='eng':
                html="<div class='eng-notes'>"
                return html
            else:
                html = ""
                return html 
                
        if context == 'end':
            if type == "lev3":
                html = "</div>"
                return html
            if type=='nodiadau':
                html = "</div>"
                return html
            if type=='cym':
                html="</div>"
                return html
            if type=='eng':
                html="</div>"
                return html
            else:
                html = ""
                return html
    
def head(element, context,args):
    if context=="begin":
        html ='<div class="title">'
        return html
    if context=="end":
        html = '</div>'
        return html

def lg(element, context, args):
    html=""
    try:
        type = element.get_attribute_value('type')
    except:
        if context=="begin":
            html = '<div class="line-group">'
            return html
        if context=="end":
            html = '</div><br/>'
            return html
    else:
        if context=="begin": 
            if type=="CNB":
                html = '<div class="CNB-group">'
                return html
            if type=="CH":
                html = '<div class="CH-group">'
                return html
            if type=="clog":
                html = '<div class="clog-group">'
                return html                                
            if type=="cywydd":
                html = '<div class="cywydd-group">'
                return html
            if type=="EP":
                html = '<div class="EP-group">'
                return html
            if type=="EUU":
                html = '<div class="EUU-group">'
                return html
            if type=="stanza":
                html = '<div class="stanza">'
                return html
            if type=="TC":
                html = '<div class="TC-group">'
                return html
            if type=="nodyn_brig":
                html = '<div class="nodyn_brig">'
                return html
            if type=="olnod":
                html = '<div class="olnod">'
                return html
            #this 'if' can be removed once all references to title have been removed    
            if type=="title":
                html = '<div class="cywydd-group">'
                return html
                
        if context=="end":
                html = '</div><br/>'
                return html

def countLeftSiblings(element, gi):
    count = 1
    try:
        while 1:
            element = element.get_previous_sibling_by_name(gi)
            count += 1
    except:
        return count        
        
def printLineNum(n):
    #check if line number is a multiple of 4   
    if int(n) % 4 == 0:
        n = n
    else:
        n = '&nbsp;'
    return n

def oddEven(n):
    #check if line number odd or even
    if int(n) % 2 == 0:
        html = '<span class="CH-line-number">' + printLineNum(n) + '</span><span class="CH-line-even">'
    else:
        html = '<span class="CH-line-number">' + printLineNum(n) + '</span><span class="CH-line-odd">'
    return html

def l(element, context, args):        
    
    lg = element.get_parent_element()
    div = lg.get_parent_element()
    divID = div.get_attribute_value('xml:id')
    poemDiv = div.get_parent_element()
    poemID = poemDiv.get_attribute_value('xml:id')
    
    #Remove selected text in xml:ids
    poemID = poemID.replace("top", "")
    poemID = poemID.replace("Guto", "")
    
    #Remove all text at the end of the manuscript ID's after the '_' character
    titleSeperator = '_'    
    divID = divID.split(titleSeperator,1)[0]
    
    #test if <lg> element has a type attribute and then get the value of the attribute
    try:
        lgType = lg.get_attribute_value("type")
    except:
        lgType = ''      
    
    #if there is a type element then count the left siblings
    lineNumber = countLeftSiblings(element, 'l')
          
    #get line number and assign to variable
    try:
        lNum = element.get_attribute_value('n')      
    except:
        lNum = ''      
             
    if context=="begin":
        if lgType == "":
            html = '<span class="variant-line">'
            return html
        elif lgType == "stanza":
            html = '<span class="variant-title">' + divID + '</span><br/><span class="variant-line-number">' + lNum + '</span><span class="variant-line">'               
            return html
                
        else:
            html = '<span class="line-number">' + lNum + '</span><span class="line">'
            return html       
    
    if context=="end":
        html = '</span><br/><br/>'               
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
            
def add(element, context, args):
    if context =="begin":
        html = '<sup>'
        return html
    if context=="end":
        html = '</sup>'
        return html
        
def delete(element, context, args):
    if context =="begin":
        html = '<strike>'
        return html
    if context=="end":
        html = '</strike>'
        return html        

def unclear(element, context, args):
    if context =="begin":
        html = '<i>'
        return html
    if context=="end":
        html = '</i>'
        return html    
    
    
def list(element, context, args):
    type = element.get_attribute_value('type')
    if context=="begin":             
        if type=='ordered':
            html='<ol>' 
            return html
        elif type=='bulleted':
            html='<ol>' 
            return html
        elif type=='simple':
            html='<ul>' 
            return html        
                               
    if context=="end":              
        if type=='ordered':
            html='</ol>' 
            return html
        elif type=='bulleted':
            html='<ol>' 
            return html
        elif type=='simple':
            html='</ul>' 
            return html        

def item(element, context, args):
    if context=="begin":             
            html='<li>' 
            return html
                               
    if context=="end":              
            html='</ul>' 
            return html

def note(element, context, args):
    if context=="begin":             
            html='<span>' 
            return html
                               
    if context=="end":              
            html='</span>' 
            return html       
        