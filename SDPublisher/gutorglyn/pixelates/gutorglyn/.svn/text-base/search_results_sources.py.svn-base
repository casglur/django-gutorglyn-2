
PIXELISE_PATTERNS = {
    'l': 'l',
    'lg': 'lg',    
}

def l(element, context, args):        
          
    #get line number and assign to variable
    try:
        lNum = element.get_attribute_value('n')      
    except:
        lNum = ''      
#              
#     searchResultLeader = 'Poem #' + poemIDclean + '<br/>'
    
    if context=="begin":  
        html = '<span class="line-number">' + lNum + '</span><span class="search-results-line">'
        return html       
    
    if context=="end":
        html = '</span><br/>'
        return html

def lg(element, context, args):

#     poemDiv = poemDiv.get_parent_element()
    poemID = element.get_attribute_value('xml:id')
    poemTitleValue = element.get_attribute_value('title')
#     poemTitleValue = div.get_child('head')        
# 
    poemID = poemID.replace("top", "")
    poemID = poemID.replace("Guto", "")  
#     
#         
#     poemIDclean = ""    
#     if poemID.startswith("0"):
#         poemIDclean = poemID.lstrip("0")
#     else:
#         poemIDclean = poemID    
    
    html=""
    if context=="begin":
        html = '<a href="/gutorglyn/poem/?poem-selection=' + poemID + '"><strong>' + str(poemTitleValue) + '</strong></a>&nbsp;<a href="/gutorglyn/poem/?poem-selection=' + poemID + '"><img alt="goto poem" src="/static/img/icons/goto-icon.png" width="16px" height="16px"></a><br/><div class="line-group">' 
        return html
    if context=="end":
        html = '</div><br/>'
        return html         
    
        