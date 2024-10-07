
from bsddb3.db import *
from dbxml import *

mgr = XmlManager()
container = mgr.openContainer("../../../gutorglyn.bdbxml")

ucontext = mgr.createUpdateContext()

indexspec = container.getIndexSpecification()

# indexspec.addIndex("http://www.tei-c.org/ns/1.0", "l", "node-element-substring-string")
indexspec.addIndex("http://www.tei-c.org/ns/1.0", "lg", "node-element-substring-string")

try:
    container.setIndexSpecification(indexspec, ucontext)

except:
    print 'cannot add index'    

print 'Index Added!'

del container
