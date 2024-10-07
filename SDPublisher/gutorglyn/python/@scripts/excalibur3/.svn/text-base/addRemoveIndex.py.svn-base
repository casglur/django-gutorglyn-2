
from bsddb3.db import *
from dbxml import *

mgr = XmlManager()
container = mgr.openContainer("../../../gutorglyn.bdbxml")

ucontext = mgr.createUpdateContext()

indexspec = container.getIndexSpecification()

indexspec.deleteIndex("http://www.sleepycat.com/2002/dbxml", "person", "unique-node-metadata-equality-string")

# indexspec.addIndex("", "person", "node-attribute-equality-string")

container.setIndexSpecification(indexspec, ucontext)

del container

print 'done!'


