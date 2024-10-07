from pixelise.core import Collection

"""Create your XML Element Processors here."""

PIXELISE_PATTERNS = {
    'div': 'div',
    'p': 'p',
    'list': 'list',
    'lb': 'lb',
    'item': 'item',
    'body/div/head': 'head1',
    'body/div/div/head': 'head2',
    'body/div/div/div/head': 'head3',
    'body/div/div/div/div/head': 'head4',
    'table': 'table',
    'row': 'row',
    'cell': 'cell',
    'seg': 'seg',
    'xref': 'xref',
    'hi': 'hi',
}

def div(element, state, context):
    """Div elements are common, but not required."""
    if state == 'begin':
        # Do something
        pass

    if state == 'end':
        # Do something
        pass

def head1(element, context,args):
	if context=="begin":
		html ='<h2>'
		return html
	if context=="end":
		html = '</h2>'
		return html

def head2(element, context,args):
	if context=="begin":
		html = '<h2 id="%s">' % (element.get_parent_element().get_attribute_value('n'))
		return html
	if context=="end":
		html = '</h2>'
		return html

def head3(element, context,args):
	if context=="begin":
		html ='<h3 id="%s">' % (element.get_parent_element().get_attribute_value('n'))
		return html
	if context=="end":
		html ='</h3>'
		return html

def head4(element, context,args):
	if context=="begin":
		html ='<h4>'
		return html
	if context=="end":
		html ='</h4>'
		return html
		

def p(element, context, args):
    html=""
    try:
    	rend = element.get_attribute_value('rend')
    except:
        if context=="begin":
        	html = '<p class="text">'
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
	
def list(element, context, args):
	if context=="begin":
		html="<UL>"
		return html
	if context=="end":
		html="</UL>"
		return html
		
def table(element, context, args):
	if context=="begin":
		html='<table class="sep" border="1">\r'
		return html
	if context=="end":
		html="</table>"
		return html

def row(element, context, args):
	if context=="begin":
		html="<tr>"
		return html
	if context=="end":
		html="</tr>\r"
		return html

def cell(element, context, args):
	if context=="begin":
		html='<td valign="top">'
		return html
	if context=="end":
		html="</td>"
		return html

def seg(element, context, args):
	if context=="begin" and element.get_attribute_value('rend')=='red':
		html='<font color="red">'
		return html
	if context=="end" and element.get_attribute_value('rend')=='red':
		html="</font>"
		return html

def item(element, context, args):
	html=""
	try:
		rend = element.get_attribute_value('rend')
	except:
		if context=="begin":
			html = '<LI>'
		if context=="end":
			html = '</LI>'
	else:
		if context=="begin":
			if rend=="cont":
				html='<p class="item">'
			else:
				html = '<p class="%s">' % (rend)
		if context=="end":
			html="</p>"
	return html
	
		
def lb(element, context, args):
	html=""
	if context=="begin":
		try:
			rend = element.get_attribute_value('rend')
		except:
			html='<br/>'
		else:
			if rend=="indent1":
				html='<br/>&nbsp;&nbsp;&nbsp;&nbsp;'
			if rend=="indent2":
				html='<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
			if rend=="indent3":
				html='<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
	return html

def xref(element, context, args):
	rend = element.get_attribute_value('rend')
	if context=="begin":
		html='<a href="%s">' % (rend)
		return html
	if context=="end":
		html='</a>'
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

