#  Copyright (C) 2007 Andrew West <andrew@keybordcowboy.co.uk>
#
#  This file is part of Pixelise.
#
#  Pixelise is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pixelise is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.

#  You should have received a copy of the GNU Lesser General Public License
#  along with Pixelise.  If not, see <http://www.gnu.org/licenses/>.

"""Pixelise is an XML/document publishing system.

This module provides helper functions that provide various 
information about elements, for example, attributes, child and parent.
"""

__author__ = 'Andrew West'
__author_email__ = 'andrew@keybordcowboy.co.uk'
__copyright__ = 'Copyright (C) 2007-2008 Andrew West'
__url__ = 'http://launchpad.net/pixelise'
__license__ = 'LGPL 3.0'
__credits__ = 'Andrew West, Zeth'


from pixelise import PixeliseTemplateException 

def match_element(element, template):
    """ Given an element, checks the template to see if any of the
        patterns match all or part of the element path."""
    if template is None:
        return None
    func = None
    pathparts = element.create_path()
    #Remove any blank at the start
    if len(pathparts) > 0 and pathparts[0] == '':
        pathparts = pathparts[1:]
    for i in range(0, len(pathparts)):
        tmppath = ""
        for j in range(i, len(pathparts)):
            tmppath = tmppath + "/" + pathparts[j]
        #Check to see if this function exists in the template pattern
        if hasattr(template, "PIXELISE_PATTERNS") == False:
            raise PixeliseTemplateException(
                "Pixelise template does not contain" + \
                    "a PIXELISE_PATTERNS definition.")
        for key in template.PIXELISE_PATTERNS:
            #Let's match nicely, a PIXELISE_PATTERNS of
            #pb,/pb,//pb will all match the same element
            if key == tmppath or \
                key == tmppath.lstrip('/') or \
               key == '/'+tmppath:
                #Found the path!
                func = template.PIXELISE_PATTERNS[key]
                break
    if func != None and hasattr(template, func):
        func = getattr(template, func)
    else:
        func = None
    return func

def get_element_by_handle(pixelise_instance, handle):
    """ Given a XmlValue Handle, returns the Xml Node """
    query = 'dbxml:handle-to-node("%s", "%s")' \
        % (pixelise_instance.pixelise_database, handle)
    results = pixelise_instance.complex_query(query)
    if results.hasNext():
        return results.next()
    else:
        return None


