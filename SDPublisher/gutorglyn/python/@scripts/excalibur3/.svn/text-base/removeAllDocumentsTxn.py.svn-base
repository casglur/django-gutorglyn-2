from bsddb3.db import *
from dbxml import *

print 'Deleting all docs!'


myenv = DBEnv()
myenv.open("../../../../gutorglyn", DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN, 0)
mgr = XmlManager(myenv, 0)

container = mgr.openContainer("../../../gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
txn = mymgr.createTransaction()
results = container.getAllDocuments(txn,0)
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