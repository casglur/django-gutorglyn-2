# -*- coding: UTF-8 -*-

import inspect

PIXELISE_PATTERNS = {
    'patron': 'patron'
}

    
def patron(element, context, args):
    attr_id = element.get_attribute_value('id')
    if context=="begin":
        html ="<a href='/gutorglyn/name-full/?n=" + attr_id + "'>"
        return html
    if context=="end":
        html = "</a><br/>"
        return html
    