from bsddb3.db import *
from dbxml import *


mgr = XmlManager()

fileRange = range(1,10)

docName = "guto115.xml"

container = mgr.openContainer("..//gutorglyn.bdbxml")
ucontext = mgr.createUpdateContext()
container.deleteDocument(docName, ucontext)
print 'Removing: ' + str(docName)
    
del container  
    
print 'Finished!'
    