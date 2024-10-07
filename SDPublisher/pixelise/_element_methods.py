#  Copyright (C) 2007-8 Andrew West <andrew@keybordcowboy.co.uk>, 
#  Zeth <theology@gmail.com)
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

This module extends the dbxml.XmlValue class with a little sanity and our own 
high level methods.

These methods are not designed to be called directly from this module. 
Rather, they are available from the XmlValue objects found in your 
pixelise.core.Collection objects.
"""

__author__ = 'Andrew West, Zeth'
__author_email__ = 'andrew@keybordcowboy.co.uk, theology@gmail.com'
__copyright__ = 'Copyright (C) 2007-2008 Andrew West, Zeth Green'
__url__ = 'http://launchpad.net/pixelise'
__license__ = 'LGPL 3.0'
__credits__ = 'Andrew West, Zeth, Peter Robinson'

import dbxml
from pixelise import PixeliseElementSearchError, PixeliseAttributeError
    
def __str__(self):
    """Return a string representation of the XML Value."""
    representation = self.asString()
    if representation.startswith('{}'):
        return representation.lstrip('{}')
    else:
        return representation

dbxml.XmlValue.__str__ = __str__

def isspace(self):
    """Return true if the node is just spaces or tabs."""
    return self.getNodeValue().isspace()

dbxml.XmlValue.isspace = isspace

def get_attribute(self, name):
    """Finds the attribute with the name 'name'.
       Returns the attribute value as an XmlValue."""
    attributes = self.getAttributes()
    while attributes.hasNext():
        attribute = attributes.next()
        attname = attribute.getNodeName()
        if attname == name:
            return attribute 
    raise PixeliseAttributeError, \
        "This %s element does not have an attribute %s." % \
            (self.getLocalName(), name)

dbxml.XmlValue.get_attribute = get_attribute

def get_attribute_value(self, name):
    """Given an XmlValue, finds the attribute with the name 'name'.
       Returns the attribute value."""
    attributes = self.getAttributes()
    while attributes.hasNext():
        attr = attributes.next()
        attname = attr.getNodeName()
        attvalue = attr.getNodeValue()
        if attname == name:
            return attvalue
    raise PixeliseAttributeError, \
        "This %s element does not have an attribute %s." % \
            (self.getLocalName(), name)

dbxml.XmlValue.get_attribute_value = get_attribute_value

def get_attribute_names(self):
    """Given an XmlValue, finds all the attribute names.
       Returns a list of the attribute names or
       None if there are no attributes"""

    attributes = self.getAttributes()
    attributenames = []
    while attributes.hasNext():
        attribute = attributes.next()
        attname = attribute.getNodeName()
        attributenames.append(attname)
    if len(attributenames) == 0:
        return None
    else:
        return attributenames

dbxml.XmlValue.get_attribute_names = get_attribute_names

def create_path(self):
    """ Returns the full path of the element as a list"""
    #if type(self) != dbxml.XmlValue:
    #    raise TypeError
    element = self 
    elpath = []
    try:
        while element and type(element) == dbxml.XmlValue \
                and element.getType() != dbxml.XmlValue.NONE:
            elpath.append(element.getLocalName())
            element = element.getParentNode()
    except dbxml.XmlException, inst:
        from pixelise import PixeliseTemplateException
        raise PixeliseTemplateException(inst)
    elpath.reverse()
    return elpath

dbxml.XmlValue.create_path = create_path

def print_element_debug(self):
    """ Print out an XML debugging value """
    if type(self) is not dbxml.XmlValue \
        or self.getType() is dbxml.XmlValue.NONE:
        return ""
    if self.getNodeType() == dbxml.XmlValue.ELEMENT_NODE:
        string = "<%s" % self.getNodeName()
        attributes = self.getAttributes()
        for attribute in attributes:
            attribute_name = attribute.getNodeName()
            attribute_value = attribute.getNodeValue()
            string = string + " %s=\"%s\"" % (attribute_name, attribute_value)
        string = string + " handle=\"%s\"" % self.getNodeHandle()
        string = string + ">"
    else:
        return self.asString()
    return string

dbxml.XmlValue.print_element_debug = print_element_debug

def get_next_node(self, ignore_child = False):
    """ Given an XmlValue, iterates through it's children, then it's 
        siblings, then it's ancestors until it find the next node 
        in sequence """
    
    #Check we're dealing with something, if not return
    if self.getType() is dbxml.XmlValue.NONE:
        return self

    #if this is a bit of text, move on to the next sibling 
    #else get the child
    if self.getNodeName() == '#text':
        next_node = self.getNextSibling()
    elif not ignore_child:
        next_node = self.getFirstChild()
        #If not child, try a sibling
        if next_node.getType() is dbxml.XmlValue.NONE:
            next_node = self.getNextSibling()
    else:
        next_node = self.getNextSibling()

    if next_node.getType() is dbxml.XmlValue.NONE:
        # No next sibling, so let's go up until we get one
        parent_node = self.getParentNode()
        while parent_node.getType() is not dbxml.XmlValue.NONE and \
                parent_node.getNextSibling().getType() is dbxml.XmlValue.NONE:
            parent_node = parent_node.getParentNode()
        if parent_node.getType() is not dbxml.XmlValue.NONE:
            next_node = parent_node.getNextSibling()
        else:
            next_node = parent_node

    return next_node 

dbxml.XmlValue.get_next_node = get_next_node

def get_next_element(self, node_name=None):
    """ Iterates through the element's siblings, then it's
        ancestors until it find the next element in sequence. """
    try:
        next_element = get_next_node(self)
    except PixeliseElementSearchError:
            raise PixeliseElementSearchError, \
                "There is no next element! You are at the end of the document"
    if node_name is None:
        return next_element
    next_element = self.get_next_node()
    while next_element.getType() is not dbxml.XmlValue.NONE and\
            next_element.getNodeName() == '#text':
        next_element = next_element.get_next_node()
    if next_element.isNull():        
        raise PixeliseElementSearchError, "There is no next element."
    return next_element

dbxml.XmlValue.get_next_element = get_next_element

def get_next_element_by_name(self, node_name): 
    """ Given an element, iterates through it's siblings, then it's
        ancestors until it find the next element in sequence that matches
        the node name given."""
    try:
        next_element = get_next_node(self)
    except PixeliseElementSearchError:
            raise PixeliseElementSearchError, \
                "There is no next element! You are at the end of the document"
    while next_element.getType() is not dbxml.XmlValue.NONE \
            and next_element.getNodeName() != node_name:
        try:
            next_element = get_next_node(next_element)
        except PixeliseElementSearchError:
            raise PixeliseElementSearchError, \
                "There is no next element called %s." % node_name
    return next_element

dbxml.XmlValue.get_next_element_by_name = get_next_element_by_name

def get_previous_node(self):
    """ Given an XmlValue, iterates through it's children, then it's 
        siblings, then it's ancestors until it find the previous node 
        in sequence """
    
    #Check we're dealing with something, if not return
    if self.getType() is dbxml.XmlValue.NONE:
        return self

    if self.getPreviousSibling().getType() is not dbxml.XmlValue.NONE:
        previous_node = self.getPreviousSibling()
    else:
        previous_node = self.getParentNode()
        return previous_node

    #There's a previous node, but we want the last child/next
    if previous_node is not dbxml.XmlValue.NONE and \
            previous_node.getLastChild().getType() is not dbxml.XmlValue.NONE:
        previous_node = previous_node.getLastChild()
        while previous_node.getNextSibling().getType() is not \
                dbxml.XmlValue.NONE or previous_node.getLastChild().getType() \
                is not dbxml.XmlValue.NONE:
            if previous_node.getNextSibling().getType() \
                    is not dbxml.XmlValue.NONE:
                previous_node = previous_node.getNextSibling()
            else:
                previous_node = previous_node.getLastChild()

    return previous_node 

dbxml.XmlValue.get_previous_node = get_previous_node

def get_previous_element(self, node_name=None):
    try:
        previous_element = get_previous_node(self)
    except PixeliseElementSearchError:
            raise PixeliseElementSearchError, \
                "There is no previous element! You are at the end of the document"
    if node_name is None:
        return previous_element
    """ Iterates through the XmlValue's siblings, then it's
        childs until it find the next element in sequence. """
    previous_element = self.get_previous_node()
    while previous_element.getType() is not dbxml.XmlValue.NONE and\
            previous_element.getNodeName() == '#text':
        previous_element = previous_element.get_previous_node()
    if previous_element.isNull():        
        raise PixeliseElementSearchError, "There is no previous element."
    return previous_element

dbxml.XmlValue.get_previous_element = get_previous_element

def get_previous_element_by_name(self, node_name): 
    """ Given an XmlValue, iterates through it's siblings, then it's
        ancestors until it find the previous element in sequence that matches
        the node name given."""
    previous_element = get_previous_element(self)
    while previous_element.getType() is not dbxml.XmlValue.NONE \
            and previous_element.getNodeName() != node_name:
        try:
            previous_element = get_previous_node(previous_element)
        except PixeliseElementSearchError:
            raise PixeliseElementSearchError, \
                "There is no previous element called %s." % node_name
    return previous_element

dbxml.XmlValue.get_previous_element_by_name = get_previous_element_by_name

def get_parent_by_name(self, node_name):
    """ Gets a parent element with the given name."""
    parent_element = self.getParentNode()
    while parent_element.getType() is not dbxml.XmlValue.NONE \
            and parent_element.getNodeName() != node_name:
        parent_element = parent_element.getParentNode()
    if parent_element.isNull():        
        raise PixeliseElementSearchError, \
            "There is no parent named %s." % node_name
    return parent_element

dbxml.XmlValue.get_parent_by_name = get_parent_by_name

def get_first_child(self):
    """Gets the first child."""
    child_node = self.getFirstChild()
    if child_node.isNull():        
        raise PixeliseElementSearchError, "There is no child."
    return child_node

dbxml.XmlValue.get_first_child = get_first_child

def get_last_child(self):
    """Gets the last child """
    child_node = self.getLastChild()
    if child_node.isNull():
        raise PixeliseElementSearchError, "There is no child."
    return child_node

dbxml.XmlValue.get_last_child = get_last_child

def get_previous_sibling(self):
    """Gets the previous sibling."""
    previous_sibling = self.getPreviousSibling()
    if previous_sibling.isNull():
        raise PixeliseElementSearchError, "There is no previous sibling."
    return previous_sibling

dbxml.XmlValue.get_previous_sibling = get_previous_sibling

def get_next_sibling(self):
    """Gets the next sibling."""
    next_sibling = self.getNextSibling()
    if next_sibling.isNull():
        raise PixeliseElementSearchError, "There is no next sibling."
    return next_sibling

dbxml.XmlValue.get_next_sibling = get_next_sibling

def get_next_sibling_by_name(self, node_name):
    """Gets the next sibling by name."""
    next_sibling = self.get_next_sibling()
    while next_sibling.getNodeName() != node_name and \
            next_sibling.getType() is not dbxml.XmlValue.NONE:
        try:
            next_sibling = next_sibling.get_next_sibling()
        except PixeliseElementSearchError:
            raise PixeliseElementSearchError, \
                "There is no next sibling with that name."    
    return next_sibling

dbxml.XmlValue.get_next_sibling_by_name = get_next_sibling_by_name

def get_previous_sibling_by_name(self, node_name):
    """Gets the previous sibling by name."""
    previous_sibling = self.get_previous_sibling()
    while previous_sibling.getNodeName() != node_name and \
            previous_sibling.getType() is not dbxml.XmlValue.NONE:
        try:
            previous_sibling = previous_sibling.get_previous_sibling()
        except PixeliseElementSearchError:
            raise PixeliseElementSearchError, \
                "There is no previous sibling with that name."    
    return previous_sibling

dbxml.XmlValue.get_previous_sibling_by_name = get_previous_sibling_by_name

def get_child(self, node_name = None):
    """ Gets first child element 
    in the first level of children only.
    If child_name is specified, then only return first element with
    that name."""
    child_element = self.get_first_child()
    if node_name is None:
        return child_element

    # Check the first child in case we got lucky
    if child_element.getNodeName() == node_name:
        return child_element
    
    # Go through the siblings on this level
    try:
        sibling_element = child_element.get_next_sibling_by_name(node_name)
    except PixeliseElementSearchError:
        raise PixeliseElementSearchError, "Not found in level 1"
    else:
        return sibling_element

dbxml.XmlValue.get_child = get_child


def get_child_by_name(self, node_name):
    """ Gets a child element with the given name
    in the first level of children only.
    Deprecated: use get_child with name parameter"""
    child_element = self.get_first_child()

    # Check the first child in case we got lucky
    if child_element.getNodeName() == node_name:
        return child_element
    
    # Go through the siblings on this level
    try:
        sibling_element = child_element.get_next_sibling_by_name(node_name)
    except PixeliseElementSearchError:
        raise PixeliseElementSearchError, "Not found in level 1"
    else:
        return sibling_element

dbxml.XmlValue.get_child_by_name = get_child_by_name

def get_parent_element(self):
    """Gets the parent element or node."""
    parent_node = self.getParentNode()
    if parent_node.isNull():
        raise PixeliseElementSearchError, "There is no parent."
    return parent_node

dbxml.XmlValue.get_parent_element = get_parent_element

def get_children(self, child_name = None):
    """Gets a list of the immediate children of an element or node.
    If child_name is specified, then only return elements with
    that name."""
    children = []
    try:
        sibling = self.get_first_child()
    except PixeliseElementSearchError:
        raise PixeliseElementSearchError, "There are no children."
    while sibling:
        if child_name:
            if sibling.get_node_name() == child_name:
                children.append(sibling)
        else:
            children.append(sibling)
        try:
            sibling = sibling.get_next_sibling()
        except PixeliseElementSearchError:
            # No more siblings so lets end the while loop
            sibling = None
    return children

dbxml.XmlValue.get_children = get_children

def get_descendant_by_name(self, child_name):
    """Get a child by name.
    Goes recursively through the children and grandchildren."""
    descendants = self.get_children()
    while descendants:
        descendant = descendants.pop(0)
        if descendant.getNodeName() == child_name:
            return descendant
        try:
            descendants.extend(descendant.get_children())
        except PixeliseElementSearchError:
            continue
        except AttributeError:
            the_type = type(descendant)
            assert False, the_type
    raise PixeliseElementSearchError, \
        "The %s was not found in the children." % child_name

dbxml.XmlValue.get_descendant_by_name = get_descendant_by_name

def get_node_name(self):
    """Gets the node name."""
    node_name = self.getNodeName()
    return node_name

dbxml.XmlValue.get_node_name = get_node_name

def get_node_value(self):
    """Gets the node value."""
    node_value = self.getNodeValue()
    return node_value

dbxml.XmlValue.get_node_value = get_node_value


# Deprecated, replaced by new get_child_by_name
def _get_child_by_name(self, pixelise_instance, name):
    """ Given an XmlValue, checks for child element with the given name """
    query = 'dbxml:handle-to-node("%s", "%s")//%s' \
        % (pixelise_instance.pixelise_database, self.getNodeHandle(), name)
    results = pixelise_instance.complex_query(query)
    if results.hasNext():
        return results.next()
    else:
        raise PixeliseElementSearchError, "There is no child called %s." % name
dbxml.XmlValue._get_child_by_name = _get_child_by_name 

# Deprecated, replaced by get_parent_by_name
def _get_ancestor_by_name(self, pixelise_instance, name):
    """ Given an XmlValue, checks for child element with the given name """
    query = 'dbxml:handle-to-node("%s", "%s")/ancestor::%s' \
        % (pixelise_instance.pixelise_database, self.getNodeHandle(), name)
    results = pixelise_instance.complex_query(query)
    if results.hasNext():
        return results.next()
    else:
        raise PixeliseElementSearchError, \
            "There is no ancestor called %s." % name
dbxml.XmlValue._get_ancestor_by_name = _get_ancestor_by_name

# Depreciated by_name methods
dbxml.XmlValue.get_children_by_name = get_children

