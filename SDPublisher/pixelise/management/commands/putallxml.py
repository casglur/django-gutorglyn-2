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
    make_option('--directory', '-d', dest='xmldirectory',
                help='Puts all xml files within the directory.'),
    make_option('--extension', '-e', dest='extension',
                help='Specify the extension of the files to be imported.'),
    )

    def handle_app(self, app, **options):
        """Load the XML into the app's XML database. """
        if options['extension']:
            target_extension = ".%s" % options['extension']
        else:
            target_extension = '.xml'
        xml_manager = XmlManager()
        update_context = xml_manager.createUpdateContext()
        # Get the app_name
        app_name = app.__name__.partition('.')[-1].rpartition('.')[0]
        # Find the XML database, Open the container
        containers = ContainerDict()
        container = xml_manager.openContainer(containers[app_name])

        # Load the XML directory
        os.chdir(options['xmldirectory'])
        xml_files = []
        for directory in os.walk('.'):
            for filename in directory[2]:
                extension = os.path.splitext(filename)[1]
                # Only import xml files
                if extension != target_extension:
                    continue
                # recontruct the path
                xml_files.append(os.path.join(directory[0], filename)
                    )
        
        for xml_source_file in xml_files:
            # Put the Xml
            _load_document(os.path.normpath(xml_source_file),
                           options['xmldirectory'],
                           container,
                           update_context)

def _load_document(document_name,
                   document_path,
                   container, 
                   update_context):
    """Load a document into the database."""
    # Put the Xml document into the database

    document = open(os.path.join(document_path, document_name))
    try:
        container.putDocument(document_name,
                              document.read(),
                              update_context
                              )
    except XmlUniqueError:
        print  "The xml file %s is already in the database. Skipped." \
            % document_name 
