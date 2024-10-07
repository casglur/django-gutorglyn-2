"""This Command is a manage.py command 
for loading an XML file into your collection."""

import os
from django.core.management.base import AppCommand
from optparse import make_option
from dbxml import XmlManager, XmlUniqueError
from pixelise.core import ContainerDict

BOOK_CONTEXT = r"<book><title>Knowledge Discovery in Databases.</title></book>"

class Command(AppCommand):
    """"Put the xml file into the xml database from given app name(s)."""
    help = "Put the xml file into the xml database from given app name(s)."

    output_transaction = True
    option_list = AppCommand.option_list + (
    make_option('--file', '-f', dest='filename',
                help='Inputs the filename into the collection.'),
    make_option('--name', '-n', dest='documentname',
                help='Give the document a name other than the default.'),
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

        # Load the XML file
        document = open(options['filename'])
        
        if options['documentname']:
            document_name =  options['documentname']
        else:
            document_name = app_name

        # Put the Xml
        try:
            container.putDocument(document_name,
                                  document.read(),
                                  update_context
                                  )
        except XmlUniqueError:
            print options['filename'] + " is already in the database. Skipped." 
