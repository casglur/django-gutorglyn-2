
import inspect


PIXELISE_PATTERNS = {                                      
    'p': 'p',
    'note':'note',
}  

def p(element, context, args):
    html=""
    
    if context=="begin":
        html = '<p>'
    if context=="end":
        html = '</p>'

    return html                

def note(element, context, args):
    poemID = None
    
    try:
        poemID = element.get_attribute_value('xml:id')
        poemTitleValue = element.get_attribute_value('title')
    
        poemID = poemID.replace("esboniadol", "")
        poemID = poemID.replace("Guto", "")
    except:
        poemID = ""
        poemTitleValue = ""       
            
    html=""
    if context=="begin":
        if poemID == "":
            html = ""
        else:
            html = '<a href="/gutorglyn/poem/?poem-selection=' + poemID + '"><strong>' + str(poemTitleValue) + '</strong></a>&nbsp;<a href="/gutorglyn/poem/?poem-selection=' + poemID + '"><img alt="goto poem" src="/static/img/icons/goto-icon.png" width="16px" height="16px"></a><br/><div class="line-group">' 
        return html

    if context=="end":
        if poemID == "":
            html = ""
        else: 
            html = '</div><br/>'
        return html   
        