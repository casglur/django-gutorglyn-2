"""Create your XML Element Processors here."""

PIXELISE_PATTERNS = {
    'div': 'div',
    'p': 'p',
    'div/head': 'head',
    'body/div/div/div/head': 'head3',
    'lg': 'lg',  
    'l': 'l',
    'hi': 'hi',
}

def div(element, state, context):
    """Div elements are common, but not required."""
    if state == 'begin':
        html = "<p>"
        return html
        # Do something
        pass

    if state == 'end':
        html = "<p>"
        return html
        # Do something
        pass

def head(element, context,args):
    if context=="begin":
        html ='<h2 style="display:none;">'
        return html
    if context=="end":
        html = '</h2>'
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
            html = '<span style="position: relative; left: 3cm;">'
            return html
        if context=="end":
            html = '</span><br/>'
            return html
    else:
        if context=="begin":            
            if type=="EP":
                html = '<span style="position: relative; left: 3cm;">'
                return html
            if type=="EUU":
                html = '<span style="position: relative; left: 3cm;">'
                return html
            if type=="TC":
                html = '<span style="position: relative; left: 2.5cm;">'
                return html
            if type=="CH":
                html = '<span style="position: relative; left: 2cm;">'
                return html
            if type=="CNB":
                html = '<span style="position: relative; left: 2.5cm;">'
                return html
        if context=="end":
                html = '</span><br/>'
                return html

def countLeftSiblings(element, gi):
    count = 1
    try:
        while 1:
            element = element.get_previous_sibling_by_name(gi)
            count += 1
    except:
        return count

def l(element, context, args): 
    lg = element.get_parent_element()
    lgChildren = lg.get_children()
    
    try:
        lgType = lg.get_attribute_value("type")
    except:
        if context=="begin":
            html = '<span>'
            return html
        if context=="end":
            html = '</span><br/>'
            return html
    else:
        lineNumber = countLeftSiblings(element, 'l')
        
    try:
        lNum = element.get_attribute_value('n')      
    except:
        lNum  = ""

    
    if context=="begin":
        if lgType == "EP":
                html = '<span>'          
                return html
            
        elif lgType == "EUU":                
            if lineNumber == 1:
                html = '<span style="position: relative; left: -1.5cm;">'
                return html
            if lineNumber == 2:
                html = '<span style="position: relative; left: 0.5cm;">'
                return html
            else:
                html = '<span>'
                return html
        
        elif lgType == "TC":
                html = '<span>'               
                return html
        
        elif lgType == "CH":                
            if lineNumber == 1:
                html = '<span style="position: relative; left: -0.5cm;">'
                return html
            else:
                html = '<span>'
                return html
            
        elif lgType == "CNB":                
                html = '<span>'
                return html        
        else:
            html = "<span>"
            return html
    if context=="end":
        html = lNum + "</span><br/>"
        return html
              
def hi(element, context, args):
    rend = element.get_attribute_value('rend')
    if context=="begin":
        if rend=='bold':
            html='<b>' 
            return html
    if context=="end":
        if rend=='bold':
            html='</b>' 
            return html
  
    
    
    