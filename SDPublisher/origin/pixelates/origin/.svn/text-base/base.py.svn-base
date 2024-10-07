"""Create your XML Element Processors here."""

PIXELISE_PATTERNS = {
     'div': 'div',
     'p':'p',
     'head': 'head',
     'pb': 'pb',
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

def head(element, state, context):
    isbookhead = False
    html = ""
    div = element.get_parent_element()
    try:
        if div.get_attribute_value('type') == "book":
            isbookhead = True
    except:
        return
    else:
        if state == 'begin' and isbookhead:
            html = "<H1>"
        if state == 'end' and isbookhead:
            html = "</H1>"
    return html

def pb(element, state, context):
     id = element.get_attribute_value('id')
     if id[0] == 'E':
         return {'stop_processing':True}
