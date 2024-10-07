from bsddb3.db import *
from dbxml import *

print 'Deleting all docs!'

mgr = XmlManager()

container = mgr.openContainer("../../../gutorglyn.bdbxml")
results = container.getAllDocuments(0)
for value in results:
    document = value.asDocument()
    #print document.getName()
    docname = document.getName()
    ucontext = mgr.createUpdateContext()
    container.deleteDocument(docname, ucontext)
    print 'Removing: ' + str(docname)

    del ucontext

del container  

print 'Finished!' 