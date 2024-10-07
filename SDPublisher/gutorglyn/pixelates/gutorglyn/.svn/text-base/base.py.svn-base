"""Create your XML Element Processors here."""

import inspect

PIXELISE_PATTERNS = {
    'add': 'add',                     
    'cell':'cell',   
    'del': 'delete',                      
    'div': 'div',
    'div/head': 'head',  
    'figure':'figure',
    '//figure/head':'imgHead',    
    'hi': 'hi',
    'item':'item',          
    'l': 'l',    
    'lb': 'lb',  
    'list':'textlist',  
    'lg': 'lg',  
    'name':'name',    
    'note':'note',      
    'p': 'p',
    'row':'row',
    'table':'table',    
    'ref':'ref',
    'unclear':'unclear',    
}

def add(element, context, args):
    if context =="begin":
        html = '<sup>'
        return html
    if context=="end":
        html = '</sup>'
        return html

def cell(element, context, args):
    if context=="begin":             
            html='<td>' 
            return html                       
    
    if context=="end":              
            html='</td>' 
            return html
        
def countLeftSiblings(element, gi):
    count = 1
    try:
        while 1:
            element = element.get_previous_sibling_by_name(gi)
            count += 1
    except:
        return count          

def delete(element, context, args):
    if context =="begin":
        html = '<del>'
        return html
    if context=="end":
        html = '</del>'
        return html   

def div(element, context, args):
    html = ""
    try:
        attr_type = element.get_attribute_value('type')
    except:
        if context == "begin":
            html = ''
            return html
        if context == "end":
            html = ''
            return html        
    else: 
        if context == 'begin':              
            if attr_type == "lev3":
                html = "<div class='transcription'>"
                return html
            if attr_type=='nodiadau':
                html = "<div class='notes'>"
                return html
            if attr_type=='cym':
                html="<div class='cym-notes'>"
                return html
            if attr_type=='eng':
                html="<div class='eng-notes'>"
                return html
            else:
                html = ""
                return html 
                
        if context == 'end':
            if attr_type == "lev3":
                html = "</div>"
                return html
            if attr_type=='nodiadau':
                html = "</div>"
                return html
            if attr_type=='cym':
                html="</div>"
                return html
            if attr_type=='eng':
                html="</div>"
                return html
            else:
                html = ""
                return html

def figure(element, context, args):
    graphicType = element.get_attribute_value('type')    
    graphicNode = element.get_child('graphic')
    graphicNodeSrc = graphicNode.get_attribute_value('url')
    descriptionNode = element.get_child('head')
    
    graphicDir = None
    if graphicType == 'llun':
        graphicDir = 'photos'
    if graphicType == 'ach':
        graphicDir = 'lineage'
    if graphicType == 'stema':
        graphicDir = 'stemma'
    
    if context=="begin":        
        html='<p><a href="/static/img/%s/%s" target="_blank"><img alt="stema" style="border-style:solid; border-color: #A20A1B #3D3D3D #3D3D3D #A20A1B; width:90%%;" src="/static/img/%s/%s"></a><br/>' % (graphicDir,graphicNodeSrc,graphicDir,graphicNodeSrc)
        return html
    if context=="end":              
        html='</p>' 
        return html
    
def head(element, context,args):
    if context=="begin":
        html ='<div class="title">'
        return html
    if context=="end":
        html = '</div>'
        return html

def hi(element, context, args):
    rend = element.get_attribute_value('rend')
    parent_element = element.get_parent_element().get_node_name()
    
    if context=="begin":             
        if rend=='bold':
            html='<b>' 
            return html        
        elif rend=='italics':
            html='<i>'
            return html
        elif rend=='poem-quote' and parent_element == 'p':
            html='</p><blockquote class="poem-quote">'
            return html             
        elif rend=='prose-quote' and parent_element == 'p':
            html='</p><blockquote>'
            return html            
        elif rend=='subscript':
            html='<sub>'
            return html   
        elif rend=='superscript':
            html='<sup>'
            return html                     
        elif rend=='underline':
            html='<u>'
            return html                        
    
    if context=="end":              
        if rend=='bold':
            html='</b>' 
            return html         
        elif rend=='italics':
            html='</i>'
            return html
        elif rend=='poem-quote' and parent_element == 'p':
            html='</blockquote><p>'
            return html          
        elif rend=='prose-quote' and parent_element == 'p':
            html='</blockquote><p>'
            return html             
        elif rend=='superscript':
            html='</sup>'
            return html                  
        elif rend=='underline':
            html='</u>'
            return html

def imgHead(element, context, args):
    if context=="begin":             
            html='<i>' 
            return html                       
    
    if context=="end":              
            html='</i>' 
            return html

def item(element, context, args):
    if context=="begin":             
            html='<li>' 
            return html
                               
    if context=="end":              
            html='</li>' 
            return html    

def l(element, context, args):        
    
    lg = element.get_parent_element()
    div = lg.get_parent_element()
    poemDiv = div.get_parent_element()
    poemID = poemDiv.get_attribute_value('xml:id')
    
    poemID = poemID.replace("top", "")
    poemID = poemID.replace("Guto", "")
    
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
         
    clogFirstLines =  [1,5,9,13,17,21,25,29,33,37,41,45,49,53,57,61,65,69,73,77,81,85,89,93,97,101,105]
    clogSecondLines = [2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66,70,74,78,82,86,90,94,98,102,106]
    clogThirdLines =  [3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63,67,71,75,79,83,87,91,95,99,103,107]
    clogFourthLines = [4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108]
             
    if context=="begin":
        if lgType == "":
            html = '<span class="variant-line-link">'
            return html
        
        if lgType == "bardd":
            html = '<span class="line-number">' + lNum + '</span><span class="bardd-line">'
            return html        

        elif lgType == "CH":
            html = '<span class="CH-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="CH-line-%s">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum), oddEven(lNum))                        
            return html
            
        elif lgType == "CNB":                
                html = '<span class="CNB-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="CNB-line">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                return html
                
        elif lgType == "clog":            
            if lineNumber in clogFirstLines:
                    html = '<span class="clog-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="clog-line-first">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))                    
                    return html
            
            if lineNumber in clogSecondLines:
                    html = '<span class="clog-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="clog-line-second">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                    return html  
            
            if lineNumber in clogThirdLines:
                    html = '<span class="clog-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="clog-line-third">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                    return html
                    
            if lineNumber in clogFourthLines:
                    html = '<span class="clog-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="clog-line-fourth">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                    return html                                
                    
            else:
                html = '<span class="clog-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="clog-line">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                return html                
                
        elif lgType == "cywydd":          
            #check the value of the 'n' attribute      
            if lNum == "1":
                html = '<span class="cywydd-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="cywydd-line-1">'  % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                return html

            #check the number of the current descendent <l> of the <lg> element   
            if lineNumber == 1:
                html = '<span class="cywydd-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="cywydd-line-first">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))  
                return html 
 
            else:
                html = '<span class="cywydd-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="cywydd-line">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))  
                return html                 
                
        elif lgType == "EP":
                html =  '<span class="EP-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="EP-line">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))        
                return html
            
        elif lgType == "EUU":
        #check the number of the current descendant <l> of the <lg> element
            if lineNumber == 1:
                html = '<span class="EUU-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="EUU-line-first">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                return html
            if lineNumber == 2:
                html = '<span class="EUU-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="EUU-line-second">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                return html
            
            if lineNumber == 3:
                html = '<span class="EUU-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="EUU-line-third">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                return html
            
            if lineNumber == 4:
                html = '<span class="EUU-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="EUU-line-fourth">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                return html                                 
            
            else:
                html = '<span class="EUU-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="EUU-line">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))
                return html
                
        elif lgType == "TC":
                html = '<span class="TC-line-number"><a class="variant-line-link-%s" title="Cliciwch i weld y darlleniadau amrywiol %s" href="%s,%s">%s</a></span><span class="TC-line">' % (showHide(lNum), lNum, poemID, lNum, printLineNum(lNum))               
                return html
             
        elif lgType == "stanza":
                html = '<span class="line-number">' + lNum + '</span><span class="line">'               
                return html
                
        else:
            html = '<span class="line-number">' + lNum + '</span><span class="line">'
            return html       
    
    if context=="end":          
        if lgType == "stanza":
            html = '</span><br/>'
            return html
        else:
            html = '</span><br/>'
        return html
              
def lb(element, context, args):
    if context =="begin":
        html = '<br/>'
        return html

def lg(element, context, args):
    html=""
    try:
        attributetype = element.get_attribute_value('type')
    except:
        if context=="begin":
            html = '<div class="line-group">'
            return html
        if context=="end":
            html = '</div><br/>'
            return html
    else:
        if context=="begin": 
            if attributetype=="bardd":
                html = '<div class="bardd-group">'
                return html            
            if attributetype=="CNB":
                html = '<div class="CNB-group">'
                return html
            if attributetype=="CH":
                html = '<div class="CH-group">'
                return html
            if attributetype=="clog":
                html = '<div class="clog-group">'
                return html                                
            if attributetype=="cywydd":
                html = '<div class="cywydd-group">'
                return html
            if attributetype=="EP":
                html = '<div class="EP-group">'
                return html
            if attributetype=="EUU":
                html = '<div class="EUU-group">'
                return html
            if attributetype=="stanza":
                html = '<div class="stanza">'
                return html
            if attributetype=="TC":
                html = '<div class="TC-group">'
                return html
            if attributetype=="nodyn_brig":
                html = '<div class="nodyn_brig">'
                return html
            if attributetype=="olnod":
                html = '<div class="olnod">'
                return html
            #this 'if' can be removed once all references to title have been removed    
            if attributetype=="title":
                html = '<div class="cywydd-group">'
                return html
                
        if context=="end":
                html = '</div><br/>'
                return html

def name(element, context, args):    
    nameVal = element.get_attribute_value('ref')
    nameType = element.get_attribute_value('type')    
    parentElement = element.get_parent_element()    
    
    parentElementName = parentElement.get_node_name()
    
    location = ''
    if parentElementName=="p":
        if nameType=="noddwr": 
            location='/gutorglyn/name/?n=%s' % (nameVal)
        if nameType=="lle":
            location='/gutorglyn/name/?n=%s' % (nameVal)
        if nameType=="pobl":
            location='/gutorglyn/name/?n=%s' % (nameVal)
    else:
        if nameType=="noddwyr":
            location='/gutorglyn/get-name/?personID=%s' % (nameVal)
        if nameType=="person": 
            location='/gutorglyn/get-name/?personID=%s' % (nameVal)
        if nameType=="lle":
            location='/gutorglyn/get-name/?placeID=%s' % (nameVal)    

    if context=="begin":
            html='<a class="name" target="_blank" href="%s">' % (location)
            return html
    if context=="end":              
        html='</a>' 
        return html
    
def note(element, context, args):
    if context=="begin":             
        html='' 
        return html
                               
    if context=="end":              
        html='' 
        return html

def oddEven(n):
    #check if line number odd or even
    if int(n) % 2 == 0:
        html = 'even'
    else:
        html = 'odd'
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
        
def printLineNum(n):
    #check if line number is a multiple of 4   
    if int(n) % 4 == 0:
        n = n
    else:
        n = n
        #n = '&nbsp;'
    return n

def row(element, context, args):
    if context=="begin":             
            html='<tr>' 
            return html                       
    
    if context=="end":              
            html='</tr>' 
            return html  
        
def ref(element, context, args):
    refTarget = element.get_attribute_value('target')
    
    try: 
        refType = element.get_attribute_value('type')
            
        if refType == 'external':        
            if context=="begin":             
                    html='<a target="_blank" href="%s"">' % refTarget 
                    return html                               
            if context=="end":              
                    html='</a>' 
                    return html                
        else:
            if context=="begin":             
                    html='<a class="manuscript-tab-call" href="%s" onclick="return false;">' % refTarget 
                    return html                               
            if context=="end":              
                    html='</a>' 
                    return html             
    except:
        if context=="begin":             
                html='<a class="manuscript-tab-call" href="%s" onclick="return false;">' % refTarget 
                return html                               
        if context=="end":              
                html='</a>' 
                return html

def showHide(n):
    #check if line number is a multiple of 4   
    if int(n) % 4 == 0:
        show = 'show'
    else:
        show = 'hide'
    return show       
    
def table(element, context, args):
    if context=="begin":             
            html='<table>' 
            return html                       
    
    if context=="end":              
            html='</table>' 
            return html
            
def textlist(element, context, args):
    attributetype = element.get_attribute_value('type')
    parent_element = element.get_parent_element().get_node_name()
    
    if parent_element == 'p':
        if context=="begin":             
            if attributetype =='ordered':
                html='</p><ol>' 
                return html
            elif attributetype =='bulleted':
                html='</p><ul>' 
                return html      
                                   
        if context=="end":              
            if attributetype =='ordered':
                html='</ol><p>' 
                return html
            elif attributetype =='bulleted':
                html='</ul><p>' 
                return html   
    else:
        if context=="begin":             
            if attributetype =='ordered':
                html='<ol>' 
                return html
            elif attributetype =='bulleted':
                html='</p><ul>' 
                return html      
                                   
        if context=="end":              
            if attributetype =='ordered':
                html='</ol>' 
                return html
            elif attributetype =='bulleted':
                html='</ul><p>' 
                return html           
        
def unclear(element, context, args):
    if context =="begin":
        html = '<i>'
        return html
    if context=="end":
        html = '</i>'
        return html       
              

                                      
    