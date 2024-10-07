# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *

mymgr = XmlManager()
myquery = "collection('../../../gutorglyn.bdbxml')//tei:div[@type='nodyn_noddwr' and @xml:id='nr08']/tei:div[@type='eng']"

mycontainer = mymgr.openContainer("../../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setDefaultCollection("../gutorglyn.bdbxml")
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

print 'Here are the results!:'
          
for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    print name + " - " + content

del mycontainer
