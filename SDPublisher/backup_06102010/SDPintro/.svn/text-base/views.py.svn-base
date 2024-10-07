from pixelise.core import Collection
from django.shortcuts import render_to_response

def text(request):
        p = Collection(request, 'SDPintro')
        results = p.query("//text")
        if results.hasNext():
            text = results.next()
        else:
            return render_to_response('SDPintro/error.html', {'message': "Can't find text element"})
	the_content = p.process_element(text, 'SDPintro/base.py',  None, None)
	nav_content = make_toc(text)
	return render_to_response('SDPintro/text.html', {'page_content': the_content, 'nav_content': nav_content})

def make_toc(text):
	div=text.get_child_by_name('body').get_child_by_name('div')
	div1s=div.get_children_by_name('div')
	html = "<p>"
	for this_div in div1s:
		div1_head=this_div.get_child_by_name('head')
		html += '<a href="#%s">%s %s</a>' % (this_div.get_attribute_value('n'), this_div.get_attribute_value('n'), div1_head.get_attribute_value('rend'))
		div2s=this_div.get_children_by_name('div')
		for this_div2 in div2s:
			div2_head=this_div2.get_child_by_name('head')
			html += '<br/>&nbsp;&nbsp;&nbsp;&nbsp;<a href="#%s">%s %s</a>' % (this_div2.get_attribute_value('n'), this_div2.get_attribute_value('n'), div2_head.get_attribute_value('rend'))
		html+='<br/><br/>\r'
	html +="</p>"
	return html