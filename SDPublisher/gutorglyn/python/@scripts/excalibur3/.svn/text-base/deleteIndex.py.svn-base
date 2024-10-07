
from bsddb3.db import *
from dbxml import *

mgr = XmlManager()
container = mgr.openContainer("../../../gutorglyn.bdbxml")

ucontext = mgr.createUpdateContext()

indexspec = container.getIndexSpecification()

indexspec.deleteIndex("http://www.tei-c.org/ns/1.0", "tei", "edge-element-equality-string")

container.setIndexSpecification(indexspec, ucontext)

del container

print 'done!'


