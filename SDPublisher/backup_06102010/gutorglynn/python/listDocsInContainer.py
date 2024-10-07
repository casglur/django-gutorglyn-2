
from bsddb3.db import *
from dbxml import *

mgr = XmlManager()
container = mgr.openContainer("..//gutorglynn.dbxml")
results = container.getAllDocuments(0)
for value in results:
    document = value.asDocument()
    print document.getName()
