"""This Command is a manage.py command 
for creating indicies based on an xml file."""

import os
from sets import Set
from xml.etree.ElementTree import parse
from optparse import make_option
from django.core.management.base import AppCommand
from dbxml import XmlManager, XmlUniqueError
from pixelise.core import ContainerDict

BOOK_CONTEXT = r"<book><title>Knowledge Discovery in Databases.</title></book>"

class Command(AppCommand):
    """"Create indicies for the given app name based on an xml file."""
    help = "Create indicies for the given app name based on an xml file."

    output_transaction = True
    option_list = AppCommand.option_list + (
    make_option('--file', '-f', dest='filename',
                help='Creates indicies based on this file.'),
    )

    def handle_app(self, app, **options):
        """Load the XML into the app's XML database. """
        xml_manager = XmlManager()
        update_context = xml_manager.createUpdateContext()

        # Get the app_name
        app_name = app.__name__.partition('.')[-1].rpartition('.')[0]
        # Find the XML database, Open the container
        containers = ContainerDict()
        container = xml_manager.openContainer(containers[app_name])

        # Parse the XML file.
        tree = parse(options['filename'])
        elements = tree.getiterator()
        elem_tags = Set()
        attr_tags = Set()
        for elem in elements:
            # Add the element tag to the element tags set 
            elem_tags.add(elem.tag)
            # Add each attribute tag to the attribute tags set
            for attribute in elem.attrib:
                attr_tags.add(attribute)


        for element in elem_tags:
            print "Creating index for element %s." % element
            container.addIndex('',
                               element,
                               'node-element-presence-none',
                               update_context)

        for attribute in attr_tags:
            print "Creating index for attribute %s." % attribute 
            container.addIndex('',
                               attribute,
                               'node-attribute-equality-string',
                               update_context)
