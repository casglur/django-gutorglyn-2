
import inspect


PIXELISE_PATTERNS = {
    'div/head': 'head',
}

def head(element,context,args):
    headDiv = element.get_parent_element()
    nextHeadDiv = headDiv.get_parent_element()
    optionContentVal = nextHeadDiv.get_attribute_value('xml:id')
    
    titleSeperator = '_'    
    cleanContentVal = optionContentVal.split(titleSeperator,1)[0]
    
    if context=="begin":
        html = r'<option value="' + optionContentVal + '">' + cleanContentVal
        return html
    
    if context=="content":
        return {'hide_content':True}  
    
    if context=="end":
        html = '</option>'
        return html
        
