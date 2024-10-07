"""Manage.py command for creating a new XML Collection Application."""

import os

from django.core.management.base import copy_helper, CommandError, LabelCommand

class Command(LabelCommand):
    """Creates new XML Collection Application."""
    help = "Creates a Django app directory structure for " + \
            "the given app name in the current directory."
    args = "[appname]"
    label = 'application name'

    requires_model_validation = False
    # Can't import settings during this command, because they haven't
    # necessarily been created.
    can_import_settings = False

    def handle_label(self, app_name, directory=None, **options):
        """Deal with the given label."""
        if directory is None:
            directory = os.getcwd()

        # Determine the project_name by using the basename of directory,
        # which should be the full path of the project directory (or the
        # current directory if no directory was passed).
        project_name = os.path.basename(directory)
        if app_name == project_name:
            raise CommandError("You cannot create an app with the same name"
                               " (%r) as your project." % app_name)

        # Check that the app_name cannot be imported.
        try:
            __import__(app_name)
        except ImportError:
            pass
        else:
            raise CommandError("%r conflicts with the name of an existing " + \
                               "Python module and cannot be used as " + \
                               "an app name. Please try another name." \
                               % app_name)

        copy_helper(self.style, 'app', app_name, directory, project_name)
        self.create_xml_database(app_name, directory)

    def create_xml_database(self, app_name, directory):
        """Create the XML Database and the stub pixelate."""
        from dbxml import XmlManager #, XmlException, DATABASE_ERROR
        xml_manager = XmlManager()

        #update_context = xml_manager.createUpdateContext()
        file_name = app_name + ".dbxml"
        file_dir = os.path.join(directory, app_name)
        full_file_name = os.path.join(file_dir, file_name)

        # Create the Database
        container = xml_manager.createContainer(full_file_name)

        # Create the pixelate directory
        pixelate_dir = os.path.join(file_dir, "pixelates")
        os.mkdir(pixelate_dir)

        # Create the pixelise stub
        pixelate_stub_file = os.path.join(pixelate_dir, 'base.py')
        import pixelise
        template_file = os.path.join(pixelise.__path__[0], 
                                     'templates', 'base.py')
        template = open(template_file, 'r')
        pixelate_stub = open(pixelate_stub_file, 'w')
        pixelate_stub.write(template.read())
        pixelate_stub.close()
        template.close()
