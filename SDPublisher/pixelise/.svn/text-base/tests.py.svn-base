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

This module provides unit tests for pixelise core.
"""

__author__ = 'Andrew West'
__author_email__ = 'andrew@keybordcowboy.co.uk'
__copyright__ = 'Copyright (C) 2007-2008 Andrew West'
__url__ = 'http://launchpad.net/pixelise'
__license__ = 'LGPL 3.0'
__credits__ = 'Andrew West, Zeth'

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from dbxml import XmlException, XmlValue

from pixelise.core import Collection
import unittest

settings.PIXELISE_DEBUG = True

class PixeliseTestCase( unittest.TestCase ):
    """A test case for Pixelise."""
    docname1 = 'xml1'
    xml1 = r'<list id="testlist"><item id="test-1">one</item>' + \
        r'<item id="test-2">two</item><item id="test-3">three</item>' + \
        r'<item id="test-4">four</item></list>'
    xmlresultstop1 = r'<list id="testlist"><item id="test-1">one</item>'
    xmlstop1 = r'<list id="testlist"><item id="test-1">one'
    xmltext1 = 'onetwothreefour'
    xmlempty = r'<div><div><ab><pb />on<lb />e<w>two</w></ab></div>' + \
        r'<div><ab><w>three</w><w>fo<pb/>ur</w></ab></div></div>'

    def setUp(self):
        """ Setup up the pixelise database and clear out our test document """
        settings.PIXELISE_DATABASE = 'test.dbxml'
        settings.PIXELISE_TEMPLATE_DIRS = None
        pixelise_instance = Collection()
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        #Get all the documents out of the container
        results = xcontainer.getAllDocuments(0)
        for result in results:
            xcontainer.deleteDocument(result.asDocument(), update_context)

    def test_initialise_sans_settings(self):
        """ Tests to see what happens if Pixelise in initalised \
        without PIXELISE_DATABASE being set, this should fail \
        by raising an exception"""
        settings.PIXELISE_DATABASE = ''
        try: 
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            pass
        else:
            self.fail("Pixelise was initalised without configuration")

    def test_initialise_settings(self):
        """ Tests to see what happens if Pixelise in initalised \
        with PIXELISE_DATABASE being set, this should not fail"""
        try: 
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not initalise")

    def test_get_xml_manager(self):
        """ Trys to get a XmlManager instance """
        try: 
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not initalise")
        try:
            xml_manager = pixelise_instance.get_xml_manager()
        except ImproperlyConfigured:
            self.fail("Could not get XmlManager")
        if xml_manager is None:
            self.fail("Could not get XmlManager")

    def test_get_container(self):
        """ Trys to get a dbXML Container instance """
        try: 
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not initalise")
        xcontainer = pixelise_instance.get_container()
        if xcontainer is None:
            self.fail("Could not get Container")

    def test_insert_xml(self):
        """ Tests entering XML into the database """
        try: 
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not initalise")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xml1, update_context)
        except XmlException, inst:
            result = "Could  not insert document into dbXML \"%\"" % (inst.What)
            self.fail(result)
        #Let's check the document is actually in there
        #First check the dbxml query, this should work
        query_collection = mgr.createQueryContext()
        try:
            results = mgr.query('collection("test.dbxml")', query_collection)
        except XmlException, inst:
            result = "Could not query dbXML \"%s\"" % (inst.What)
            self.fail(result)
        results.reset()
        #Should be only one result
        self.assertEqual(1, results.size())
        result = results.next()
        self.assertEqual(self.docname1, result.asDocument().getName())
        self.assertEqual(self.xml1, result.asString())
        #Now try using Pixelises query
        results = pixelise_instance.query("")
        results.reset()
        #Should be only one result
        #Can't check the size of lazy evaluated results
        result = results.next()
        self.assertEqual(self.docname1, result.asDocument().getName())
        self.assertEqual(self.xml1, result.asString())

    def test_query_element(self):
        """ Tests querying XML elements with Pixelise """
        try:
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not initalise")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xml1, update_context)
        except XmlException, inst:
            result = "Could  not insert document into dbXML \"%\"" % (inst.What)
            self.fail(result)
        results = pixelise_instance.query('//item')
        #Check we have some results
        if not results or not results.hasNext():
            self.fail("Pixelise did not return any results")

    def test_query_element(self):
        """ Tests querying XML elements with Pixelise """
        try:
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not initalise")
        results = pixelise_instance.query('//item')
        #Check we have some results
        if not results:
            self.fail("Pixelise did not return any results")

    def test_process_element(self):
        """ Tests process XML elements with Pixelise """
        try: 
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not initalise")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xml1, update_context)
        except XmlException, inst:
            result = "Could  not insert document into dbXML \"%\"" % (inst.What)
            self.fail(result)
        #Grab the first element
        results = pixelise_instance.query('//list', None, 1, 1)
        element = results.next()
        #Shouldn't work first time because we haven't specified
        #A template directory
        try:
            text = pixelise_instance.process_element(element, 'testpixelate.py')
        except ImproperlyConfigured:
            settings.PIXELISE_TEMPLATE_DIRS = ('pixelates',)
        else:
            self.fail("Template Directory should not be configured yet")
        #Try again
        try:
            text = pixelise_instance.process_element(element, 'testpixelate.py')
        except ImproperlyConfigured, inst:
            result = "Problem calling process_element \"%s\"" % (inst)
            self.fail(result)
        self.assertEqual(self.xmltext1, text)
        #Now test the pattern matching
        try:
            text = pixelise_instance.process_element(element,
                                                    'testcomplexpixelate.py')
        except ImproperlyConfigured, inst:
            result = "Problem calling process_element \"%s\"" % (inst)
            self.fail(result)
        self.assertEqual(self.xml1, text)

    def test_stop_process_element(self):
        """ Tests stopping process XML elements with Pixelise """
        try: 
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not initalise")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xml1, update_context)
        except XmlException, inst:
            result = "Could  not insert document into dbXML \"%\"" % (inst.What)
            self.fail(result)
        #Grab the first element
        results = pixelise_instance.query('//list', None, 1, 1)
        element = results.next()
        settings.PIXELISE_TEMPLATE_DIRS = ('pixelates',)
        try:
            text = pixelise_instance.process_element(element,
                                                    'testresultstoppixelate.py')
        except ImproperlyConfigured, inst:
            result = "Problem calling process_element \"%s\"" % (inst)
            self.fail(result)
        self.assertEqual(self.xmlresultstop1, text)
        #Try again without returning any ouput
        try:
            text = pixelise_instance.process_element(element,
                                                    'teststoppixelate.py')
        except ImproperlyConfigured, inst:
            result = "Problem calling process_element \"%s\"" % (inst)
            self.fail(result)
        self.assertEqual(self.xmlstop1, text)

    def test_empty_process_element(self):
        """ Tests empty element processing with Pixelise """
        try: 
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not initalise")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xmlempty, update_context)
        except XmlException, inst:
            result = "Could not insert document into dbXML \"%s\"" % (inst.What)
            self.fail(result)
        #Grab the first element
        results = pixelise_instance.query('//pb', None, 1, 1)
        element = results.next()
        settings.PIXELISE_TEMPLATE_DIRS = ('pixelates',)
        try:
            text = pixelise_instance.process_element(element, None, 
                                                    None, True)
        except ImproperlyConfigured, inst:
            result = "Problem calling process_element \"%s\"" % (inst)
            self.fail(result)
        self.assertEqual(self.xmltext1, text)

    def test_process_single_element(self):
        """ Test processing a single element """
        try: 
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not initalise")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xml1, update_context)
        except XmlException, inst:
            result = "Could not insert document into dbXML \"%s\"" % (inst.What)
            self.fail(result)
        #Grab the first element
        results = pixelise_instance.query('//item', None, 1, 1)
        item = results.next()
        self.assertNotEqual(item.getType(), XmlValue.NONE)
        self.assertEqual(item.getNodeName(), 'item')
        self.assertEqual(item.get_attribute_value('id'), 'test-1')

        item_text = pixelise_instance.process_element(item)
        self.assertEqual(item_text, "one")


class PiXMLTestCase( unittest.TestCase ):

    docname1 = 'xml1'
    xml1 = r'<list id="testlist-1"><item id="test-1">on<pb/>e</item>' + \
            r'<list id="testlist-2"><item id="test-2">two</item>' + \
            r'<item id="test-3">three</item></list>' + \
            r'<item id="test-4">four</item></list>'

    def setUp(self):
        """ Setup up the pixelise database and clear out our test document """
        settings.PIXELISE_DATABASE = 'test.dbxml'
        settings.PIXELISE_TEMPLATE_DIRS = None
        pixelise_instance = Collection()
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        #Get all the documents out of the container
        results = xcontainer.getAllDocuments(0)
        for result in results:
            xcontainer.deleteDocument(result.asDocument(), update_context)

    def test_get_next_node(self):
        """ Tests get next node with Pixelise """
        try:
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not be initalised")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xml1, update_context)
        except XmlException, inst:
            result = "Could  not insert document into dbXML \"%\"" % (inst.What)
            self.fail(result)
        #Grab an element
        results = pixelise_instance.query("//list[@id='testlist-1']")
        if not results or not results.hasNext():
            self.fail("Could not find list element")
        list1 = results.next()
        self.assertNotEqual(list1.getType(), XmlValue.NONE)
        self.assertEqual(list1.getNodeName(), 'list')
        self.assertEqual(list1.get_attribute_value('id'), 'testlist-1')
        #Grab the next node, should be item@test-1
        item1 = list1.get_next_node()
        self.assertNotEqual(item1.getType(), XmlValue.NONE)
        self.assertEqual(item1.getNodeName(), 'item')
        self.assertEqual(item1.get_attribute_value('id'), 'test-1')
        #Grab the next node, should be text (on)
        text1 = item1.get_next_node()
        self.assertNotEqual(text1.getType(), XmlValue.NONE)
        self.assertEqual(text1.getNodeName(), '#text')
        self.assertEqual(text1.asString(), 'on')
        #Grab the next node, should be a pb
        pb1 = text1.get_next_node()
        self.assertNotEqual(pb1.getType(), XmlValue.NONE)
        self.assertEqual(pb1.getNodeName(), 'pb')
        #Grab the next node, should be text (e)
        text2 = pb1.get_next_node()
        self.assertNotEqual(text2.getType(), XmlValue.NONE)
        self.assertEqual(text2.getNodeName(), '#text')
        self.assertEqual(text2.asString(), 'e')
        #Grab the next node, should be list
        list2 = text2.get_next_node()
        self.assertNotEqual(list2.getType(), XmlValue.NONE)
        self.assertEqual(list2.getNodeName(), 'list')
        self.assertEqual(list2.get_attribute_value('id'), 'testlist-2')
        #Grab the next node, should be item 
        item2 = list2.get_next_node()
        self.assertNotEqual(item2.getType(), XmlValue.NONE)
        self.assertEqual(item2.getNodeName(), 'item')
        self.assertEqual(item2.get_attribute_value('id'), 'test-2')
        #Grab the next node, should be text 
        text2 = item2.get_next_node()
        self.assertNotEqual(text2.getType(), XmlValue.NONE)
        self.assertEqual(text2.getNodeName(), '#text')
        self.assertEqual(text2.asString(), 'two')
        #Grab the next node, should be item 
        item3 = text2.get_next_node()
        self.assertNotEqual(item3.getType(), XmlValue.NONE)
        self.assertEqual(item3.getNodeName(), 'item')
        self.assertEqual(item3.get_attribute_value('id'), 'test-3')
        #Grab the next node, should be text 
        text3 = item3.get_next_node()
        self.assertNotEqual(text3.getType(), XmlValue.NONE)
        self.assertEqual(text3.getNodeName(), '#text')
        self.assertEqual(text3.asString(), 'three')
        #Grab the next node, should be item 
        item4 = text3.get_next_node()
        self.assertNotEqual(item4.getType(), XmlValue.NONE)
        self.assertEqual(item4.getNodeName(), 'item')
        self.assertEqual(item4.get_attribute_value('id'), 'test-4')
        #Grab the next node, should be text 
        text4 = item4.get_next_node()
        self.assertNotEqual(text4.getType(), XmlValue.NONE)
        self.assertEqual(text4.getNodeName(), '#text')
        self.assertEqual(text4.asString(), 'four')
        #Should be no, next node
        no_node = text4.get_next_node()
        self.assertEqual(no_node.getType(), XmlValue.NONE)

    def test_get_next_node_ignore_child(self):
        """ Tests get next node with ignore child option in Pixelise """
        try:
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not be initalised")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xml1, update_context)
        except XmlException, inst:
            result = "Could  not insert document into dbXML \"%\"" % (inst.What)
            self.fail(result)
        #Grab an element
        results = pixelise_instance.query("//item[@id='test-1']")
        if not results or not results.hasNext():
            self.fail("Could not find list element")
        item1 = results.next()
        self.assertNotEqual(item1.getType(), XmlValue.NONE)
        self.assertEqual(item1.getNodeName(), 'item')
        self.assertEqual(item1.get_attribute_value('id'), 'test-1')
        #Grab the next node, should be item@test-1
        list2 = item1.get_next_node(True)
        self.assertNotEqual(list2.getType(), XmlValue.NONE)
        self.assertEqual(list2.getNodeName(), 'list')
        self.assertEqual(list2.get_attribute_value('id'), 'testlist-2')


    def test_get_next_element(self):
        """ Tests get next element with Pixelise"""
        try:
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not be initalised")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xml1, update_context)
        except XmlException, inst:
            result = "Could  not insert document into dbXML \"%\"" % (inst.What)
            self.fail(result)
        #Grab an element
        results = pixelise_instance.query("//list[@id='testlist-1']")
        list1 = results.next()
        self.assertNotEqual(list1.getType(), XmlValue.NONE)
        self.assertEqual(list1.getNodeName(), 'list')
        self.assertEqual(list1.get_attribute_value('id'), 'testlist-1')
        #Grab the next node, should be item@test-1
        item1 = list1.get_next_element()
        self.assertNotEqual(item1.getType(), XmlValue.NONE)
        self.assertEqual(item1.getNodeName(), 'item')
        self.assertEqual(item1.get_attribute_value('id'), 'test-1')
        #Grab the next node, should be pb
        pb1 = item1.get_next_element()
        self.assertNotEqual(pb1, XmlValue.NONE)
        self.assertEqual(pb1.getNodeName(), 'pb')
        #Grab the next node, should be list@testlist-1
        list2 = pb1.get_next_element()
        self.assertNotEqual(list2.getType(), XmlValue.NONE)
        self.assertEqual(list2.getNodeName(), 'list')
        self.assertEqual(list2.get_attribute_value('id'), 'testlist-2')
        #Grab the next node, should be item@test-2
        item2 = list2.get_next_element()
        self.assertNotEqual(item2.getType(), XmlValue.NONE)
        self.assertEqual(item2.getNodeName(), 'item')
        self.assertEqual(item2.get_attribute_value('id'), 'test-2')
        #Grab the next node, should be item@test-3
        item3 = item2.get_next_element()
        self.assertNotEqual(item3.getType(), XmlValue.NONE)
        self.assertEqual(item3.getNodeName(), 'item')
        self.assertEqual(item3.get_attribute_value('id'), 'test-3')
        #Grab the next node, should be item@test-3
        item4 = item3.get_next_element()
        self.assertNotEqual(item4.getType(), XmlValue.NONE)
        self.assertEqual(item4.getNodeName(), 'item')
        self.assertEqual(item4.get_attribute_value('id'), 'test-4')
        #Should be no, next node
        no_node = item4.get_next_element()
        self.assertEqual(no_node.getType(), XmlValue.NONE)

    def test_get_previous_node(self):
        """ Tests get previous node with Pixelise """
        try:
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not be initalised")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xml1, update_context)
        except XmlException, inst:
            result = "Could  not insert document into dbXML \"%\"" % (inst.What)
            self.fail(result)
        #Grab an element
        results = pixelise_instance.query("//item[@id='test-4']")
        if not results or not results.hasNext():
            self.fail("Could not find list element")
        item4 = results.next()
        self.assertNotEqual(item4.getType(), XmlValue.NONE)
        self.assertEqual(item4.getNodeName(), 'item')
        self.assertEqual(item4.get_attribute_value('id'), 'test-4')
        #Now get the previous node, should be text three
        text3 = item4.get_previous_node()
        self.assertNotEqual(text3.getType(), XmlValue.NONE)
        self.assertEqual(text3.getNodeName(), '#text')
        self.assertEqual(text3.asString(), 'three')
        #Previous node, should be item test-3
        item3 = text3.get_previous_node()
        self.assertNotEqual(item3.getType(), XmlValue.NONE)
        self.assertEqual(item3.getNodeName(), 'item')
        self.assertEqual(item3.get_attribute_value('id'), 'test-3')
        #Previous node, should be text two
        text2 = item3.get_previous_node()
        self.assertNotEqual(text2.getType(), XmlValue.NONE)
        self.assertEqual(text2.getNodeName(), '#text')
        self.assertEqual(text2.asString(), 'two')
        #Previous node, should be item test-2
        item2 = text2.get_previous_node()
        self.assertNotEqual(item2.getType(), XmlValue.NONE)
        self.assertEqual(item2.getNodeName(), 'item')
        self.assertEqual(item2.get_attribute_value('id'), 'test-2')
        #Previous node, should be list test-2
        list2 = item2.get_previous_node()
        self.assertNotEqual(list2.getType(), XmlValue.NONE)
        self.assertEqual(list2.getNodeName(), 'list')
        self.assertEqual(list2.get_attribute_value('id'), 'testlist-2')
        #Previous node, should be #text e
        text_e = list2.get_previous_node()
        self.assertNotEqual(text_e.getType(), XmlValue.NONE)
        self.assertEqual(text_e.getNodeName(), '#text')
        self.assertEqual(text_e.asString(), 'e')
        #Previous node, should be pb 
        pb = text_e.get_previous_node()
        self.assertNotEqual(pb.getType(), XmlValue.NONE)
        self.assertEqual(pb.getNodeName(), 'pb')
        #Previous node, should be #text on
        text_on = pb.get_previous_node()
        self.assertNotEqual(text_on.getType(), XmlValue.NONE)
        self.assertEqual(text_on.getNodeName(), '#text')
        self.assertEqual(text_on.asString(), 'on')
        #Previous node, should be item
        item1 = text_on.get_previous_node()
        self.assertNotEqual(item1.getType(), XmlValue.NONE)
        self.assertEqual(item1.getNodeName(), 'item')
        self.assertEqual(item1.get_attribute_value('id'), 'test-1')
        #Previous node, should be list 
        list1 = item1.get_previous_node()
        self.assertNotEqual(list1.getType(), XmlValue.NONE)
        self.assertEqual(list1.getNodeName(), 'list')
        self.assertEqual(list1.get_attribute_value('id'), 'testlist-1')
        #Previous node, should be document 
        doc = list1.get_previous_node()
        self.assertNotEqual(doc.getType(), XmlValue.NONE)
        self.assertEqual(doc.getNodeName(), '#document')
        #Previous node, should be document 
        no_element = doc.get_previous_node()
        self.assertEqual(no_element.getType(), XmlValue.NONE)

    def test_get_previous_element(self):
        """ Tests get previous node with Pixelise """
        try:
            pixelise_instance = Collection()
        except ImproperlyConfigured:
            self.fail("Pixelise could not be initalised")
        #Small bit of set up required
        #Create the manager
        mgr = pixelise_instance.get_xml_manager()
        #Get an create/update context
        update_context = mgr.createUpdateContext()
        #Grab the container
        xcontainer = pixelise_instance.get_container()
        try:
            #Put the document in
            xcontainer.putDocument(self.docname1, self.xml1, update_context)
        except XmlException, inst:
            result = "Could  not insert document into dbXML \"%\"" % (inst.What)
            self.fail(result)
        #Grab an element
        results = pixelise_instance.query("//item[@id='test-4']")
        if not results or not results.hasNext():
            self.fail("Could not find list element")
        item4 = results.next()
        self.assertNotEqual(item4.getType(), XmlValue.NONE)
        self.assertEqual(item4.getNodeName(), 'item')
        self.assertEqual(item4.get_attribute_value('id'), 'test-4')
        #Previous element, should be item test-3
        item3 = item4.get_previous_element()
        self.assertNotEqual(item3.getType(), XmlValue.NONE)
        self.assertEqual(item3.getNodeName(), 'item')
        self.assertEqual(item3.get_attribute_value('id'), 'test-3')
        #Previous element, should be item test-2
        item2 = item3.get_previous_element()
        self.assertNotEqual(item2.getType(), XmlValue.NONE)
        self.assertEqual(item2.getNodeName(), 'item')
        self.assertEqual(item2.get_attribute_value('id'), 'test-2')
        #Previous element, should be list test-2
        list2 = item2.get_previous_element()
        self.assertNotEqual(list2.getType(), XmlValue.NONE)
        self.assertEqual(list2.getNodeName(), 'list')
        self.assertEqual(list2.get_attribute_value('id'), 'testlist-2')
        #Previous element, should be pb 
        pb = list2.get_previous_element()
        self.assertNotEqual(pb.getType(), XmlValue.NONE)
        self.assertEqual(pb.getNodeName(), 'pb')
        #Previous element, should be item
        item1 = pb.get_previous_element()
        self.assertNotEqual(item1.getType(), XmlValue.NONE)
        self.assertEqual(item1.getNodeName(), 'item')
        self.assertEqual(item1.get_attribute_value('id'), 'test-1')
        #Previous element, should be list 
        list1 = item1.get_previous_element()
        self.assertNotEqual(list1.getType(), XmlValue.NONE)
        self.assertEqual(list1.getNodeName(), 'list')
        self.assertEqual(list1.get_attribute_value('id'), 'testlist-1')
        #Previous element, should be document 
        doc = list1.get_previous_element()
        self.assertNotEqual(doc.getType(), XmlValue.NONE)
        self.assertEqual(doc.getNodeName(), '#document')
        #Previous element, should be document 
        no_element = doc.get_previous_element()
        self.assertEqual(no_element.getType(), XmlValue.NONE)
