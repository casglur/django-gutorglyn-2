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
    'item':'item'   
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
        html ='<div class="hidden-title">'
        return html
    if context=="end":
        html = '</div>'
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
    #divID = div.get_attribute_value('xml:id')
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
            html = '<span class="variant-line">'
            return html
        
        if lgType == "CH":
            html = oddEven(lNum)
            return html
            
        elif lgType == "CNB":                
                html = '<span class="CNB-line-number">' + printLineNum(lNum) + '</span><span class="CNB-line">'
                return html
                
        elif lgType == "clog":            
            if lineNumber in clogFirstLines:
                    html = '<span class="clog-line-number">' + printLineNum(lNum) + '</span><span class="clog-line-first">'                    
                    return html
            
            if lineNumber in clogSecondLines:
                    html = '<span class="clog-line-number">' + printLineNum(lNum) + '</span><span class="clog-line-second">'
                    return html  
            
            if lineNumber in clogThirdLines:
                    html = '<span class="clog-line-number">' + printLineNum(lNum) + '</span><span class="clog-line-third">'
                    return html
                    
            if lineNumber in clogFourthLines:
                    html = '<span class="clog-line-number">' + printLineNum(lNum) + '</span><span class="clog-line-fourth">'
                    return html                                
                    
            else:
                html = '<span class="clog-line-number">' + printLineNum(lNum) + '</span><span class="clog-line">'
                return html                
                
        elif lgType == "cywydd":          
            #check the value of the 'n' attribute      
            if lNum == "1":
                html = '<span class="cywydd-line-number">' + printLineNum(lNum) + '</span><span class="cywydd-line-1"><a class="variant-line" title="Cliciwch i weld y darlleniadau amrywiol ' + lNum + '" href="#" OnClick="showLine(\'%s\',\'%s\');">' % (poemID,lNum)       
                return html

            #check the number of the current descendent <l> of the <lg> element   
            if lineNumber == 1:
                html = '<span class="cywydd-line-number">' + printLineNum(lNum) + '</span><span class="cywydd-line-first"><a class="variant-line" title="Cliciwch i weld y darlleniadau amrywiol ' + lNum + '" href="#" OnClick="showLine(\'%s\',\'%s\');">' % (poemID,lNum)               
                return html 
 
            else:
                html = '<span class="cywydd-line-number">' + printLineNum(lNum) + '</span><span class="cywydd-line"><a class="variant-line" title="Cliciwch i weld y darlleniadau amrywiol ' + lNum + '" href="#" OnClick="showLine(\'%s\',\'%s\');">' % (poemID,lNum)             
                return html                 
                
        elif lgType == "EP":
                html =  '<span class="EP-line-number">' + printLineNum(lNum) + '</span><span class="EP-line">'          
                return html
            
        elif lgType == "EUU":
        #check the number of the current descendant <l> of the <lg> element
            if lineNumber == 1:
                html = '<span class="EUU-line-number">' + printLineNum(lNum) + '</span><span class="EUU-line-first">'
                return html
            if lineNumber == 2:
                html = '<span class="EUU-line-number">' + printLineNum(lNum) + '</span><span class="EUU-line-second">'
                return html
            
            if lineNumber == 3:
                html = '<span class="EUU-line-number">' + printLineNum(lNum) + '</span><span class="EUU-line-third">'
                return html
            
            if lineNumber == 4:
                html = '<span class="EUU-line-number">' + printLineNum(lNum) + '</span><span class="EUU-line-fourth">'
                return html                                 
            
            else:
                html = '<span class="EUU-line-number">' + printLineNum(lNum) + '</span><span class="EUU-line">'
                return html
                
        elif lgType == "TC":
                html = '<span class="TC-line-number">' + printLineNum(lNum) + '</span><span class="TC-line">'               
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
            html = '</a></span><br/>'
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
    type = element.get_attribute_value('type')    
    if context=="begin":
        if type=='nodiadau_trawsysgrifiad_cym':
            html='<span>' 
            return html 
        else:            
            html='<span>' 
            return html
                               
    if context=="end":
        if type=='nodiadau_trawsysgrifiad_cym':
            html='</span><br/><br/>' 
            return html
        else:                      
            html='</span>'
            return html       
