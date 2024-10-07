"""This Command is a manage.py command 
for removing an XML file from your collection."""

import os
from django.core.management.base import AppCommand
from optparse import make_option
from dbxml import XmlManager, XmlDocumentNotFound
from pixelise.core import ContainerDict

BOOK_CONTEXT = r"<book><title>Knowledge Discovery in Databases.</title></book>"

class Command(AppCommand):
    """"Remove the xml file from the xml database from given app name(s)."""
    help = "Remove the xml file from the xml database from given app name(s)."

    output_transaction = True
    option_list = AppCommand.option_list + (
    make_option('--name', '-n', dest='documentname',
                help='Removes a document based on a document name.'),
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

        # Find the document to remove
        if options['documentname']:
            # If there is a documentname then use that
            document_name = options['documentname']
        else:
            # Otherwise try the app_name
            document_name = app_name
        
        # Remove the XML document from the collection
        try:
            container.deleteDocument(document_name,
                                     update_context
                                     )
        except XmlDocumentNotFound:
            print "The document %s is not found. Skipped." % document_name

