
from bsddb3.db import *
from dbxml import *

mgr = XmlManager()
container = mgr.openContainer("..//..//gutorglyn.bdbxml")
updateContext = mgr.createUpdateContext()
container.deleteDocument("guto126.xml", updateContext)

del container
