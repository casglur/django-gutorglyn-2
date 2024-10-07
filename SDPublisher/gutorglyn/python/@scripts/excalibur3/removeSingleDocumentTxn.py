from bsddb3.db import *
from dbxml import *

filename = "pobl.xml"

myenv = DBEnv()
myenv.open("../../../../gutorglyn", DB_INIT_TXN, 0)
mymgr = XmlManager(myenv, 0)

try:
    mycontainer = mymgr.openContainer("../../../gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
    ucontext = mymgr.createUpdateContext()
    document = str(filename)
    txn = mymgr.createTransaction()
    mycontainer.deleteDocument(txn, document, ucontext)
    txn.commit()
    print str(filename) + ' now removed!'
    del ucontext
    del txn
    del mycontainer

except XmlException, inst:
        print "XmlException (", inst.exceptionCode,"): ", inst.what
        if inst.exceptionCode == DATABASE_ERROR:
            print "Database error code:",inst.dbError

