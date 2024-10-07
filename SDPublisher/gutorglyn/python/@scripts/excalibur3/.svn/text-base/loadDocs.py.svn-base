
from bsddb3.db import *
from dbxml import *

mgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
container = mgr.openContainer("..//gutorglyn.bdbxml")
updateContext = mgr.createUpdateContext()
container.deleteDocument("guto027.xml", updateContext)

del container
