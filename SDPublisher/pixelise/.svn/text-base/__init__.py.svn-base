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

This module provides initialisation.

This pixelise.core module provides the Pixelise object.

The Pixelise object is the high level interface to the 
XML database. Here is a typical way to access your database:

from pixelise.core import Collection
collection = Collection()

"""

__author__ = 'Andrew West, Zeth'
__author_email__ = 'andrew@keybordcowboy.co.uk'
__copyright__ = 'Copyright (C) 2007-2009 Andrew West, Zeth'
__url__ = 'http://launchpad.net/pixelise'
__license__ = 'LGPL 3.0'
__credits__ = 'Andrew West, Zeth'
__version__ = '0.2beta'

class PixeliseTemplateException(Exception):
    """ Pixelise Template Exception, give when either the template
    doesn't exist, or there is an error with it."""
    pass

class PixeliseOutputLimitException(Exception):
    """ Pixelise Output Limit Exception, give when either template
    tries to output more elements than specified in the settings file."""
    pass

class PixeliseElementSearchError(Exception):
    """ Pixelise Element Search Exception, give when a query or element method
    tries to give an element outside of the available xml.
    I.e. it could not find what you are looking for."""
    pass

class PixeliseAttributeError(Exception):
    """ Pixelise Attribute Exception, give when a query or element method
    tries to give an attribute that does not exist."""
    pass


def get_version(full = False):
    """Returns the version number. Set full to True for revision id."""

    try:
        from bzrlib.branch import Branch
        from bzrlib.errors import NotBranchError
    except ImportError:
        return __version__ + "-unknown"

    # Make sure we get the correct branch location.
    # Even with symlinks
    import os
    start_dir = os.path.abspath(os.curdir)
    os.chdir(__path__[0])
    try:
        pixelise_branch = Branch.open_containing(os.path.abspath('.'))[0]
    except NotBranchError:
        os.chdir(start_dir)
        return __version__ + "-unknown"
    
    os.chdir(start_dir)
    version = __version__ + "-" + str(pixelise_branch.revno())
    if full:
        version += "-" + pixelise_branch.last_revision()
    return version
