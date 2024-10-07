from bsddb3.db import *
from dbxml import *

mymgr = XmlManager()
myquery = r"collection('../../../gutorglyn.bdbxml')//tei:note[@xml:id='e_001_027']/tei:p"



mycontainer = mymgr.openContainer("../../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")

qcontext.setDefaultCollection("../../../gutorglyn.bdbxml")

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    print name, ": ", content

del mycontainer
