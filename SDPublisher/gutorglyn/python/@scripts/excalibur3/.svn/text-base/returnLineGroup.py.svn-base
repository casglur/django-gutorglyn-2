# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *

myStr = 'y sydd i’m'
declareNamespace = 'declare namespace tei="http://www.tei-c.org/ns/1.0";'
searchFunction = 'contains($line, "%s")' % myStr
#searchFunction = '(dbxml:contains($line, "%s"))' % myStr
mymgr = XmlManager()
myquery = r'%s for $lines in collection("../../../gutorglyn.bdbxml")//tei:div[@type="lev1"]/tei:lg where some $line in $lines satisfies %s return $lines' % (declareNamespace, searchFunction)

print myquery

mycontainer = mymgr.openContainer("../../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()

qcontext.setDefaultCollection("../../../gutorglyn.bdbxml")

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    print name, ": ", content

del mycontainer
