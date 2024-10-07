
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
    
def head(element, context,args):
    if context=="begin":
        html ='<div class="title">'
        return html
    if context=="end":
        html = '</div>'
        return html        

def lg(element, context, args):
    div = element.get_parent_element()
    
    try:
        div.get_attribute_value('type')
        poemDiv = div.get_parent_element()
        poemID = poemDiv.get_attribute_value('xml:id')
        poemTitleValue = poemDiv.get_child('head') 
            
    except:
        poemDiv = div.get_parent_element()
        poemDiv = poemDiv.get_parent_element()
        poemDiv = poemDiv.get_parent_element()
        poemID = poemDiv.get_attribute_value('xml:id')
        poemTitleValue = div.get_child('head')        
    
#     poemID = div.get_attribute_value('xml:id')
#     poemTitleValue = div.get_child('head')
    
#     if poemDiv.get_attribute_value('xml:id'):
#         poemID = div.get_attribute_value('xml:id')
#         poemTitleValue = div.get_child('head')       
#     else:
#         poemID = poemDiv.get_attribute_value('xml:id')
#         poemTitleValue = poemDiv.get_child('head')

        
#     poemTitleValue = poemDiv.get_child('head')
    poemID = poemID.replace("top", "")
    poemID = poemID.replace("Guto", "")  
    
        
    poemIDclean = ""    
    if poemID.startswith("0"):
        poemIDclean = poemID.lstrip("0")
    else:
        poemIDclean = poemID    
    
    html=""
    if context=="begin":
        html = '<a href="/gutorglyn/poem/?poem-selection=' + poemID + '"><strong>' + str(poemTitleValue) + '</strong></a>&nbsp;<a href="/gutorglyn/poem/?poem-selection=' + poemID + '"><img alt="goto poem" src="/static/img/icons/goto-icon.png" width="16px" height="16px"></a><br/><div class="line-group">' 
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

def l(element, context, args):        
    
    lg = element.get_parent_element()
    div = lg.get_parent_element()
    poemDiv = div.get_parent_element()
    
    try:
        divType = div.get_attribute_value('type')
        divID = div.get_attribute_value('xml:id')    
        poemTitleValue = poemDiv.get_child('head')    
        poemID = poemDiv.get_attribute_value('xml:id')
        poemID = poemID.replace("top", "")
        poemID = poemID.replace("Guto", "")        
    except:
        poemID = ""
    
    poemIDclean = ""
    if poemID.startswith("0"):
        poemIDclean = poemID.lstrip("0")
    else:
        poemIDclean = poemID
    
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
             
    searchResultLeader = 'Poem #' + poemIDclean + '<br/>'
    
    if context=="begin":  
            html = '<a href="/gutorglyn/poem/?poem-selection=' + poemID + '"><strong>' + str(poemTitleValue) + '</strong></a><br/><span class="line-number">' + lNum + '</span><span class="search-results-line">'
            return html       
    
    if context=="end":
        html = '</span><br/><br/>'
        return html
              
def lb(element, context, args):
    if context =="begin":
        html = '<br/>'
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
        