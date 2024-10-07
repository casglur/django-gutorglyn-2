from bsddb3.db import *
from dbxml import *

#remove source files 001 - 009

fileRange = range(1,10)

for x in fileRange:
    mymgr = XmlManager()
    mycontainer = mymgr.openContainer("..//gutorglyn.bdbxml")
    ucontext = mymgr.createUpdateContext()
    document = "guto00" + str(x) + ".xml"
    mycontainer.deleteDocument(document, ucontext)
    del mycontainer

