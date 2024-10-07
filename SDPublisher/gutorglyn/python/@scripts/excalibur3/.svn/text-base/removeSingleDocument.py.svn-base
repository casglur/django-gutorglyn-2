from bsddb3.db import *
from dbxml import *

# filename = "guto057.xml"
filename = raw_input('Enter a file name: ')

mymgr = XmlManager()
mycontainer = mymgr.openContainer("../../../gutorglyn.bdbxml")
ucontext = mymgr.createUpdateContext()
document = str(filename)
mycontainer.deleteDocument(document, ucontext)
print str(filename) + ' now removed!'
del mycontainer

