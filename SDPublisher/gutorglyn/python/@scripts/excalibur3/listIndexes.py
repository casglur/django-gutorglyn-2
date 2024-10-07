
from bsddb3.db import *
from dbxml import *

mgr = XmlManager()
container = mgr.openContainer("../../../gutorglyn.bdbxml")

ucontext = mgr.createUpdateContext()

indexspec = container.getIndexSpecification()

print 'The DB contains the following indexes \n' 

for index in container.getIndexSpecification():
    print "%s (%s): %s" % (index.get_name(), index.get_uri(), index.get_index())

del container


