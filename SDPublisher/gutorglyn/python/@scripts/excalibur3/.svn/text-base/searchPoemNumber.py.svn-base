# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *

poemNum = '010'
mymgr = XmlManager()
myquery = "declare namespace tei='http://www.tei-c.org/ns/1.0';collection('../gutorglyn.bdbxml')//tei:div[@xml:id='Guto%stop']/tei:head" % poemNum

mycontainer = mymgr.openContainer("../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setDefaultCollection("../gutorglyn.bdbxml")
#qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    print name + " - " + content

del mycontainer
