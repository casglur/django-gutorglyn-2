#  Copyright (C) 2007-2009 Andrew West <andrew@keybordcowboy.co.uk>, Zeth
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

This module provides the core Pixelise Collection object.

The Collection object is the high level interface to the 
XML database. Here is a typical way to access your database:

>>> from pixelise.core import Collection
>> collection = Collection()

Pixelise supports a number of optional settings, 
which can be added to the settings.py file.

PIXELISE_OUTPUT_LIMIT to change the output limit. 
This should be an integer, e.g. 999999.

PIXELISE_TEMPLATE_DIRS to use non-default locations for the 
pixelate (xml processor) directories.
This should be a list of directory paths.

PIXELISE_DEBUG for debugging information.
This should be True or False.

"""

__author__ = 'Andrew West, Zeth'
__author_email__ = 'andrew@keybordcowboy.co.uk'
__copyright__ = 'Copyright (C) 2007-2009 Andrew West, Zeth'
__url__ = 'http://launchpad.net/pixelise'
__license__ = 'LGPL 3.0'
__credits__ = 'Andrew West, Zeth'

# Standard library
import os
from imp import load_source

# Django 
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.loading import AppCache

# DBXML
from dbxml import *


# Pixelise
from pixelise import PixeliseTemplateException 
from pixelise import PixeliseOutputLimitException
from pixelise.utils import match_element 
import pixelise._element_methods

class Collection( object ):
    """ 
    The Collection class provides access to your XML collections.
    
    You can use it as follows:
    
    >>> from pixelise.core import Collection
    >>> collection = Collection()
    
    When using the Collection class within a Django view, you can provide
    the request object as the first argument. As shown here:
    
    >>> collection = Collection(request)
    
    If you are using multiple xml applications, then you can specify the 
    app name as an argument. For example:
    
    >>> collection = Collection(request, 'myapp')
    
    """

    def __init__(self,
                 request = None, # Optional HTTP request object 
                 app = None # Optional XML Application name
                 ):

        # If there is debug info in the settings then add it to the object 
        if hasattr(settings, "PIXELISE_DEBUG"):
            self.debug = settings.PIXELISE_DEBUG
        else:
            self.debug = False
        
        # The HTTP request and response objects
        self.request = request
        self.response = None

        #The string output
        self.outputs = []

        #Count the number of elements processed
        self.processed_element = 0

        # Manager and Container
        self.manager = None
        self.container = None

        # Get the container location
        containers = ContainerDict()
        pixelise_database_path = containers[app]
        
        # Change directory to the directory containing the database
        # (Do we really need to do this? Why not just use the absolute path?)
        dirname = os.path.dirname(pixelise_database_path)
        os.chdir(dirname)
        # Trim the database name down to just the filename
        # (Do we really need to do this? Why not just use the absolute path?)
        self.pixelise_database = os.path.basename(pixelise_database_path)

        #Try connecting to the database
        self._connect()

    def _connect(self):
        """ connects to the database and opens the container """
        if self.manager is None:
            # More error checking, check the file exist
            if not os.path.exists(self.pixelise_database) or \
                not os.path.isfile(self.pixelise_database):
                raise ImproperlyConfigured("The database %s does" \
                        " not exist" % self.pixelise_database)
            #Check that the file is readable/writable by pixelise
            if not os.access(self.pixelise_database, os.R_OK):
                raise ImproperlyConfigured("The database %s is" \
                        " not readable" % self.pixelise_database)
            if not os.access(self.pixelise_database, os.W_OK):
                raise ImproperlyConfigured("The database %s is" \
                        " not writable" % self.pixelise_database)
            try:
                self.manager = XmlManager()
                self.container = self.manager.openContainer( \
                                    self.pixelise_database)
            except XmlException, xmle:
                raise ImproperlyConfigured(xmle)

    def get_xml_manager(self):
        """ Returns the dbXML database manager, if one isn't already open
            it opens and then returns it """
        if self.manager is None:
            self._connect()
        return self.manager

    def get_container(self):
        """ Returns the dbXML container, if there isn't a dbXML connection
            established this will try and connect first"""
        if self.container is None:
            self._connect()
        return self.container

    def query(self, query, start=None, end=None):
        """
        Provides the ability to access your XML 
        using XQuery or XPath expressions.
        
        >>> from pixelise.core import Collection
        >>> collection = Collection()
        >>> collection.query('//pb')
        
        Collection.querywWraps an XQuery expression into 
        something dbXML can use, supplying the container name, 
        and optionally limiting the query to a specified 
        set of results (start, end)
        """
        # DBXML fails if you give it a unicode.
        this_query = ""
        if self.manager is None:
            self._connect()
        #Add in the collection info
        this_query = "collection('" + self.pixelise_database + "')" + str(query)
        #See if we need to limit the results
        if start != None and end != None:
            this_query = "let $x := " + this_query + \
                    " return fn:subsequence($x, %i, %i)" % (start, end)
        return self._perform_query(this_query, None)

    def count(self, query, start=None, end=None):
        """
        Performs an XQuery in the same way as .query, 
        but returns the number of results instead of the results.
        
        >>> from pixelise.core import Collection
        >>> collection = Collection()
        >>> collection.count('//pb')
        
        You can optionally limit the query to a specified 
        set of results (start, end)
        """
        # DBXML fails if you give it a unicode.
        this_query = ""
        if self.manager is None:
            self._connect()
        #Add in the collection info
        this_query = "collection('" + self.pixelise_database + "')" + str(query)
        this_query = "count(%s)" % this_query
        #See if we need to limit the results
        if start != None and end != None:
            this_query = "let $x := " + this_query + \
                    " return fn:subsequence($x, %i, %i)" % (start, end)
        xml_results = self._perform_query(this_query, None)
        # Return result as integer rather than XmlResults object
        first_result = xml_results.next()
        int_result = int(first_result.asString())
        return int_result

    def complex_query(self, query, query_container=None):
        """ Unlike the normal query, this expects a full dbXML XQuery
            expression"""
        #If we don't specify a query context then create one
        return self._perform_query(query, query_container)

    def _perform_query(self, query, query_container=None):
        """ Internal method used by both query and complex_query to run
            dbXML querys"""
        #If we don't specify a query context then create one
        if query_container is None:
            mgr = self.get_xml_manager()
            query_container = mgr.createQueryContext()
            query_container.setNamespace("tei", "http://www.tei-c.org/ns/1.0")
            query_container.setNamespace("functx", "http://www.functx.com")
            query_container.setEvaluationType(query_container.Lazy)
        #Now try and execute the query
        result = None
        try:
            result = self.manager.query(query, query_container)
        except XmlQueryParserError:
            raise ImproperlyConfigured(
                "The Xquery %s appears to be invalid." % \
                    query
                )
        except XmlException, xmle:
            raise ImproperlyConfigured(xmle)
        return result

    def process_element(self,
                        element,
                        template_name = None,
                        continue_past_end = False,
                        response = None
                        ):
        """ Given an element and a template names, iterates 
            through the elements matching each element against any function"""
        if self.debug:
            print "process_element element=%s, template_name=%s, " \
                    "continue_past_end=%s" % ( element.print_element_debug(), \
                    template_name, continue_past_end )
        #Grab the options
        #if type(element) != XmlValue and type(element) != dbxml.XmlValue:
        #    raise TypeError("Expected a XmlValue but got a %s" % type(element))
        #Now iterate through the elements, child/rightsibling

        self.processed_element = 0
        if response is None:
            self.response = None
            #Append a new output to our lists of outputs.
            self.outputs.append('')
        else:
            self.response = response

        # Get the template
        if template_name != None:
            template = load_template(template_name)
        else:
            template = None

        # Set the output limit
        #We only want the second part of the return value, the first one can
        #be ignored
        self._process_element(element, template, continue_past_end)
    
        if self.response:
            return self.response
        else:
            return self.outputs.pop()
    
    def _process_element(self,
                        element, 
                        template, 
                        continue_past_end = False,
                        end_element = None):
        """ Given an XmlValue, process that element"""
        #if type(element) != XmlValue:
        #    raise TypeError("Excepted a XmlValue \
        #                    but got a %s" % element.__name__)

        self._process_element_debug(element, continue_past_end, end_element)

        this_element = element
        hide_content = False
        stop_processing = False

        if hasattr(settings, "PIXELISE_OUTPUT_LIMIT"):
            pixelise_output_limit = settings.PIXELISE_OUTPUT_LIMIT
        else:
            pixelise_output_limit = 10000

        #Over ride output limit from template if there is one
        if template and hasattr(template, "PIXELISE_OUTPUT_LIMIT"):
            pixelise_output_limit = template.PIXELISE_OUTPUT_LIMIT

        # While we are below the output limit, then process elements
        while self.processed_element < pixelise_output_limit:
            self.processed_element = self.processed_element+1

            stop_processing = self._text_or_element(this_element, template, 
                                  hide_content)

            next_element = this_element.getNextSibling()
            if next_element.getType() is XmlValue.NONE and continue_past_end:
                next_element = this_element.get_next_node(
                    continue_past_end)
            if self.debug:
                print "MOVING: _process_element from=%s, to=%s" % \
                    ( this_element.print_element_debug(), \
                    next_element.print_element_debug() )
            if next_element.getType() is XmlValue.NONE or \
                not end_element or end_element == \
                next_element.getParentNode() \
                    or stop_processing:
                #Double check that we don't want to carry on
                if next_element.getType() is XmlValue.NONE or \
                        not continue_past_end or stop_processing:
                    if self.debug:
                        print "MOVING: Not moving"
                    break
            this_element = next_element
            
        if self.processed_element >= pixelise_output_limit:
            raise PixeliseOutputLimitException("Output limit on " + \
                    "number of element processed has been reached.")

        if self.debug:
            print "FINISH: _process_element element=%s, continue_past_end=%s" \
                % ( element.print_element_debug(), continue_past_end )

        return stop_processing

    def _process_element_debug(self,
                               element,
                               continue_past_end,
                               end_element):
        """Print debug info if required."""
        if self.debug:
            print "START : _process_element element=%s, continue_past_end=%s" \
                % ( element.print_element_debug(), continue_past_end )
            if end_element:
                print "START2 : _process_element end_element=%s" \
                        % ( end_element.print_element_debug() )

    def _text_or_element(self, this_element, template, hide_content):
        """Checks element type and then processes it appropriately."""

        if self.debug:
            print "START : _text_or_element=%s, hide_content=%s" % \
                    ( this_element.print_element_debug(), hide_content )

        stop_processing = False

        if this_element.getNodeType() == XmlValue.TEXT_NODE and \
                this_element.getNodeName() != '':

            # This is a text node, i.e. some text
            # This gets written out to the web 
            self._process_text_node(this_element)

        elif this_element.getType() == XmlValue.ELEMENT_NODE or \
                this_element.getType() == XmlValue.NODE:

            # This is an element node, this gets processed.
            func = match_element(this_element, template)

            #If we find a function that matches this, perform a begin call 
            if func != None:
                self._process_element_func(template, this_element, func, \
                                            'begin')

                #if there's a function, perform a content function call
                result = self._process_element_func(template, this_element, \
                                                    func, 'content')
                hide_content = result['hide_content']

            # If there is content to hide, then lets hide it.
            if hide_content is False:
                child_element = this_element.getFirstChild()
                if child_element.getType() == XmlValue.ELEMENT_NODE or \
                    child_element.getType() == XmlValue.NODE:
                    stop_processing = self._process_element(
                                        child_element, template, False, \
                                                this_element)

            if func != None and not stop_processing:
                # If we find a function that matches this, 
                # perform an end call 
                result = self._process_element_func(template, this_element, \
                                                    func, 'end')
                stop_processing = result['stop_processing']

        if self.debug:
            print "FINISH: _text_or_element=%s, hide_content=%s, " \
                    "stop_processing=%s" % \
                    ( this_element.print_element_debug(), hide_content, \
                    stop_processing )

        return stop_processing



    def _process_text_node(self, this_element):
        """ Given a xml text element, grabs the textual content
            of the element, and puts it into the response variable """
        #Just print out the content
        if self.response:
            self.response.write(this_element.asString())
        else:
            self.outputs[-1] = self.outputs[-1] + this_element.asString()

    def _process_element_func(self, template, this_element, func, state):
        """ Given a xml element, function and arguments.
            Calls the fuction with the arguments and xml element,
            Putting the string returned (if these is one), into the response"""
        args = {'response': self.response, 'request': self.request,
                'pixelise': self}

        #Work out the template name
        template_name = template.__name__[len("Pixelate"):]

        try:
            result = func(this_element, state, args)
        except Exception, inst:
            raise PixeliseTemplateException("Problem calling " + \
                    "%s of element \"%s\" in \"%s\" %s." \
                    % (state, this_element.getNodeName(), template_name, inst))
        #The result could be a simple string, a dict or None
        output = None
        hide_content = False
        stop_processing = False
        if result != None:
            #String result
            if type(result) == type(''):
                output = result
            #Dict result
            elif type(result) == type({}):
                if result.has_key('result'):
                    output = result['result']
                if result.has_key('stop_processing'):
                    stop_processing = result['stop_processing']
                if result.has_key('hide_content'):
                    hide_content = result['hide_content']
            else:
                raise PixeliseTemplateException(\
                    "Problem calling %s of element "+ \
                    "\"%s\", the return value was a \"%s\"."\
                    % (state, this_element.getNodeName(), result))
        #Write now we might have some content, so write it out
        if output != None:
            if self.response:
                self.response.write(result)
            else:
                self.outputs[-1] = self.outputs[-1] + output
        #Return any parameters that we might have found
        return {'stop_processing': stop_processing, \
                'hide_content': hide_content}

    ### Modification methods below ###

    def add_attribute_to_element(self,
                                 query,
                                 scope,
                                 name,
                                 content,
                                 ):
        """The attribute is added to the targeted element's or elements' 
        attribute list(s).
        query = an XPath/XQuery expression of the element or elements
        that you want to change
        scope = an XmlValue or XmlResults object to provide the scope 
        of the modification. 
        i.e. The query applies to every document or documents which 
        contains the XmlValue or XmlResults object.
        This maybe should be abstracted away. I'n not sure yet.
        name = the name of the new attribute
        content = the content of the new attribute.
        """
        nodetype = XmlModify.Attribute
        self._modify(query,
                     scope,
                     name,
                     content,
                     nodetype,
                     'addAppendStep')

    def add_element_to_element(self,
                             query,
                             scope,
                             name,
                             content,
                             ):
        """Add a child element to the element after the element's 
        last existing child.
        query = an XPath/XQuery expression of the element or elements
        that you want to change
        scope = an XmlValue or XmlResults object to provide the scope 
        of the modification. 
        i.e. The query applies to every document or documents which 
        contains the XmlValue or XmlResults object.
        This maybe should be abstracted away. I'n not sure yet.
        name = the name of the new element;
        content = the content of the new element.
        """
        nodetype = XmlModify.Element
        self._modify(query,
                     scope,
                     name,
                     content,
                     nodetype,
                     'addAppendStep')

    def add_element_before_element(self,
                             query,
                             scope,
                             name,
                             content,
                             ):
        """Add a child element to the element after the element's 
        last existing child.
        query = an XPath/XQuery expression of the element or elements
        that you want to change
        scope = an XmlValue or XmlResults object to provide the scope 
        of the modification. 
        i.e. The query applies to every document or documents which 
        contains the XmlValue or XmlResults object.
        This maybe should be abstracted away. I'n not sure yet.
        name = the name of the new element;
        content = the content of the new element.
        """
        nodetype = XmlModify.Element
        self._modify(query,
                     scope,
                     name,
                     content,
                     nodetype,
                     'addInsertBeforeStep')

    def add_element_after_element(self,
                             query,
                             scope,
                             name,
                             content,
                             ):
        """Add a child element to the element after the element's 
        last existing child.
        query = an XPath/XQuery expression of the element or elements
        that you want to change
        scope = an XmlValue or XmlResults object to provide the scope 
        of the modification. 
        i.e. The query applies to every document or documents which 
        contains the XmlValue or XmlResults object.
        This maybe should be abstracted away. I'n not sure yet.
        name = the name of the new element;
        content = the content of the new element.
        """
        nodetype = XmlModify.Element
        self._modify(query,
                     scope,
                     name,
                     content,
                     nodetype,
                     'addInsertAfterStep')

    def add_text_to_element(self,
                             query,
                             scope,
                             name,
                             content,
                             ):
        """Add a child element to the element after the element's 
        last existing child.
        query = an XPath/XQuery expression of the element or elements
        that you want to change
        scope = an XmlValue or XmlResults object to provide the scope 
        of the modification. 
        i.e. The query applies to every document or documents which 
        contains the XmlValue or XmlResults object.
        This maybe should be abstracted away. I'n not sure yet.
        name = the name of the text node, this is never shown.
        content = the content of the new text.
        """
        nodetype = XmlModify.Text
        self._modify(query,
                     scope,
                     name,
                     content,
                     nodetype,
                     'addAppendStep'
                     )

    def add_text_before_element(self,
                             query,
                             scope,
                             name,
                             content,
                             ):
        """Add a child element to the element after the element's 
        last existing child.
        query = an XPath/XQuery expression of the element or elements
        that you want to change
        scope = an XmlValue or XmlResults object to provide the scope 
        of the modification. 
        i.e. The query applies to every document or documents which 
        contains the XmlValue or XmlResults object.
        This maybe should be abstracted away. I'n not sure yet.
        name = the name of the text node, this is never shown.
        content = the content of the new text.
        """
        nodetype = XmlModify.Text
        self._modify(query,
                     scope,
                     name,
                     content,
                     nodetype,
                     'addInsertBeforeStep'
                     )
        
    def add_text_after_element(self,
                             query,
                             scope,
                             name,
                             content,
                             ):
        """Add a child element to the element after the element's 
        last existing child.
        query = an XPath/XQuery expression of the element or elements
        that you want to change
        scope = an XmlValue or XmlResults object to provide the scope 
        of the modification. 
        i.e. The query applies to every document or documents which 
        contains the XmlValue or XmlResults object.
        This maybe should be abstracted away. I'n not sure yet.
        name = the name of the text node, this is never shown.
        content = the content of the new text.
        """
        nodetype = XmlModify.Text
        self._modify(query,
                     scope,
                     name,
                     content,
                     nodetype,
                     'addInsertAfterStep'
                     )

    def add_comment_to_element(self,
                               query,
                               scope,
                               name,
                               content,
                               ):
        """Add a child element to the element after the element's 
        last existing child.
        query = an XPath/XQuery expression of the element or elements
        that you want to change
        scope = an XmlValue or XmlResults object to provide the scope 
        of the modification. 
        i.e. The query applies to every document or documents which 
        contains the XmlValue or XmlResults object.
        This maybe should be abstracted away. I'n not sure yet.
        name = the name of the new comment, never shown so slightly 
        pointless.
        content = the content of the text.
        """
        nodetype = XmlModify.Comment
        self._modify(query,
                     scope,
                     name,
                     content,
                     nodetype,
                     'addAppendStep'
                     )

    def add_comment_before_element(self,
                                   query,
                                   scope,
                                   name,
                                   content,
                                   ):
        """Add a child element to the element after the element's 
        last existing child.
        query = an XPath/XQuery expression of the element or elements
        that you want to change
        scope = an XmlValue or XmlResults object to provide the scope 
        of the modification. 
        i.e. The query applies to every document or documents which 
        contains the XmlValue or XmlResults object.
        This maybe should be abstracted away. I'n not sure yet.
        name = the name of the new comment, never shown so slightly 
        pointless.
        content = the content of the text.
        """
        nodetype = XmlModify.Comment
        self._modify(query,
                     scope,
                     name,
                     content,
                     nodetype,
                     'addInsertBeforeStep'
                     )

    def add_comment_after_element(self,
                                  query,
                                  scope,
                                  name,
                                  content,
                                  ):
        """Add a child element to the element after the element's 
        last existing child.
        query = an XPath/XQuery expression of the element or elements
        that you want to change
        scope = an XmlValue or XmlResults object to provide the scope 
        of the modification. 
        i.e. The query applies to every document or documents which 
        contains the XmlValue or XmlResults object.
        This maybe should be abstracted away. I'n not sure yet.
        name = the name of the new comment, never shown so slightly 
        pointless.
        content = the content of the text.
        """
        nodetype = XmlModify.Comment
        self._modify(query,
                     scope,
                     name,
                     content,
                     nodetype,
                     'addInsertAfterStep'
                     )

    def _modify(self,
               query,
               scope,
               name,
               content,
               nodetype,
               modify_method,
               ):
        """Do something to something else.
        See appendix b of the book"""
        # Make an instance of the manager
        mymgr = self.get_xml_manager()
        # Create a query context
        qcontext = mymgr.createQueryContext()
        # Create an update context
        ucontext = mymgr.createUpdateContext()
        # Create a modification
        modification = mymgr.createModify()
        # Prepare the query expression.
        queryexp = mymgr.prepare(query, qcontext)
        # Modify the elements that match the query context
        addappendstep = getattr(modification,
                                modify_method)
        addappendstep(queryexp,
                      nodetype,
                      name,
                      content)
        #modification.addAppendStep(queryexp, nodetype, name, content)
        # execute the modification
        modification.execute(scope, qcontext, ucontext)

    def remove(self,
               query,
               scope,
               ):
        """Remove a node, such as an element, text, attribute or comment."""
        # Make an instance of the manager
        mymgr = self.get_xml_manager()
        # Create a query context
        qcontext = mymgr.createQueryContext()
        # Create an update context
        ucontext = mymgr.createUpdateContext()
        # Create a modification
        modification = mymgr.createModify()
        # Prepare the query expression.
        queryexp = mymgr.prepare(query, qcontext)
        # Modify the elements that match the query context
        modification.addRemoveStep(queryexp)
        #modification.addAppendStep(queryexp, nodetype, name, content)
        # execute the modification
        modification.execute(scope, qcontext, ucontext)


    def rename(self,
               query,
               scope,
               new_name,
               ):
        """Rename an element or attribute."""
        # Make an instance of the manager
        mymgr = self.get_xml_manager()
        # Create a query context
        qcontext = mymgr.createQueryContext()
        # Create an update context
        ucontext = mymgr.createUpdateContext()
        # Create a modification
        modification = mymgr.createModify()
        # Prepare the query expression.
        queryexp = mymgr.prepare(query, qcontext)
        # Modify the elements that match the query context
        modification.addRenameStep(queryexp, new_name)
        #modification.addAppendStep(queryexp, nodetype, name, content)
        # execute the modification
        modification.execute(scope, qcontext, ucontext)
    
    def update(self,
               query,
               scope,
               new_text):
        """Update an element or attribute."""
        #import pdb; pdb.set_trace()
        # Make an instance of the manager
        mymgr = self.get_xml_manager()
        # Create a query context
        qcontext = mymgr.createQueryContext()
        # Create an update context
        ucontext = mymgr.createUpdateContext()
        # Create a modification
        modification = mymgr.createModify()
        # Prepare the query expression.
        queryexp = mymgr.prepare(query, qcontext)
        # Modify the elements that match the query context
        modification.addUpdateStep(queryexp, new_text)
        #modification.addAppendStep(queryexp, nodetype, name, content)
        # execute the modification
        modification.execute(scope, qcontext, ucontext)


def load_template(template_name):
    """ Loads the pixelise template (pixelate), using the configuration
        PIXELISE_TEMPLATE_DIRS from the settings class"""
    #Grab the template directories
    if hasattr(settings, 'PIXELISE_TEMPLATE_DIRS') \
            and settings.PIXELISE_TEMPLATE_DIRS:
        # If there is a list specified in the template dirs, then use that
        template_dirs = settings.PIXELISE_TEMPLATE_DIRS
    else:
        # Otherwise find them in the default location
        template_dirs = []
        # Get Django's app cache
        app_cache = AppCache()
        # Look through each application
        for app in app_cache.get_apps():
            # Get the base path of the application 
            filepath = os.path.dirname(app.__file__)
            # Look for a pixelise template directory there
            pixelate_directory_path = os.path.abspath(
                                          os.path.join(filepath, 'pixelates')
                                      )
            # If there is one, add it to the list
            if os.path.exists(pixelate_directory_path):
                template_dirs.append(pixelate_directory_path)
        # If we found none, then give up.
        if not template_dirs:
            raise ImproperlyConfigured(
            """There is no pixelate directory in the default location and
             PIXELISE_TEMPLATE_DIRS is not defined.""")
    #Loop through the directories looking for the templates
    template = None
    for tdir in template_dirs:
        try:
            pathname = os.path.join(tdir, template_name)
            #Work out the basename
            file_name = os.path.split(pathname)[1]
            file_base_name = os.path.splitext(file_name)[0]
            module_name = 'Pixelate' + file_base_name 
            template = load_source(module_name, pathname)
        except IOError:
            continue
        except ImportError, inst:
            raise PixeliseTemplateException("Problem loading Pixelise " + \
                    "template %s (%s)." % (template_name, str(inst)))
        except Exception, inst:
            raise PixeliseTemplateException("Problem finding Pixelise " + \
                    "template %s (%s)." % (template_name, inst))
    if template is None:
        raise PixeliseTemplateException("Pixelise template " + \
                "%s does not exist." % template_name)
    return template

class ContainerDict(dict):
    """Dictionary of XML containers."""
    
    def __init__(self, *args, **kwargs):
        # Call the parent methods to keep the class as a true dict
        # In case this class is used in an advanced way outside Pixelise 
        dict.__init__(self)
        self.update(*args, **kwargs)
        
        self._load_apps()

    def _load_apps(self):
        """Load XML containers into a dictionary."""
        # Get Django's app cache
        app_cache = AppCache()
        # Look through each application
        for app in app_cache.get_apps():
            # Get the base path of the application 
            filepath = os.path.dirname(app.__file__)
            app_name = os.path.basename(filepath)
            # Look for a database there
            xml_database = app_name + '.bdbxml'
            xml_database_path = os.path.join(filepath, xml_database)
            xml_database_path = os.path.abspath(xml_database_path)
            # If there is one, add it to the dictionary
            if os.path.exists(xml_database_path):
                self[app_name] = xml_database_path

    def __getitem__(self, lookfor):
        """Overides Dictionary __getitem__ 
        to return a default choice for a non-existing argument,
        i.e. return something for nothing."""
        try:
            return dict.__getitem__(self, lookfor)
        except KeyError:
            if not lookfor:
                try:
                    return self.itervalues().next()
                except StopIteration:
                    message = """There is no XML application,
                    use ``python manage.py startxml name`` to create one."""
                    raise ImproperlyConfigured(message)
            else:
                raise

